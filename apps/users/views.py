"""
APPS.USERS.VIEWS
================
Vistas para el sistema de autenticación, registro y gestión de usuarios.

Este módulo contiene todas las vistas relacionadas con:
- Registro de usuarios (productores, consumidores, suplidores)
- Inicio y cierre de sesión
- Perfil de usuario (edición y visualización)
- Aprobación de productores y suplidores (ONPECO)
- Perfil público de productores
- Recuperación de contraseña
- Gestión de usuarios por ONPECO
- Cambio de contraseña temporal

Roles de usuario:
- consumidor: Comprador final
- productor: Agricultor que vende productos
- suplidor: Intermediario (desactivado)
- regulador (ONPECO): Supervisor del sistema
- acopio (Centro de Acopio): Gestión de pedidos
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import Http404, HttpResponseForbidden
from django.db import models
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from .models import User
from .forms import RegistroProductorForm, RegistroConsumidorForm, RegistroSuplidorForm, CustomPasswordResetForm
import secrets
import string


# =============================================================================
# REGISTRO DE USUARIOS
# =============================================================================

# =============================================================================
# VISTA: registro_productor
# =============================================================================
# Propósito: Permite a un usuario registrarse como productor.
# La cuenta requiere aprobación de ONPECO (is_approved = False).
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#
# Retorna:
#   - GET: Renderiza 'users/registro_productor.html' con el formulario
#   - POST: Valida, crea el usuario y redirige al login
#
# URLs asociadas:
#   - /users/registro/productor/
#
# Flujo de trabajo:
#   1. Verificar que el usuario no esté autenticado
#   2. Procesar POST con datos del formulario
#   3. Validar cédula, email y otros campos
#   4. Crear usuario con rol 'productor' y is_approved=False
#   5. Mostrar mensaje de éxito con instrucciones
# =============================================================================
def registro_productor(request):
    """
    Vista para registro de Productores
    """
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        form = RegistroProductorForm(request.POST)
        if form.is_valid():
            user = form.save()
            # No hacer login automático, redirigir a login
            messages.success(request, '✅ ¡Registro exitoso! Tu cuenta ha sido creada y será revisada por ONPECO. Recibirás una notificación cuando sea aprobada.')
            return redirect('users:login')
        else:
            messages.error(request, '❌ Por favor corrige los errores en el formulario.')
    else:
        form = RegistroProductorForm()
    
    return render(request, 'users/registro_productor.html', {'form': form})


# =============================================================================
# VISTA: registro_consumidor
# =============================================================================
# Propósito: Permite a un usuario registrarse como consumidor.
# La cuenta se aprueba automáticamente (is_approved = True).
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#
# Retorna:
#   - GET: Renderiza 'users/registro_consumidor.html'
#   - POST: Valida, crea el usuario y redirige al login
#
# URLs asociadas:
#   - /users/registro/consumidor/
#
# Flujo de trabajo:
#   1. Verificar que el usuario no esté autenticado
#   2. Procesar POST con datos del formulario
#   3. Validar cédula, email y otros campos
#   4. Crear usuario con rol 'consumidor' y is_approved=True
#   5. Mostrar mensaje de éxito
# =============================================================================
def registro_consumidor(request):
    """
    Vista para registro de Consumidores
    """
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        form = RegistroConsumidorForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '✅ ¡Registro exitoso! Bienvenido a VPJ - Venta Precio Justo. Ya puedes iniciar sesión con tus credenciales.')
            return redirect('users:login')
        else:
            messages.error(request, '❌ Por favor corrige los errores en el formulario.')
    else:
        form = RegistroConsumidorForm()
    
    return render(request, 'users/registro_consumidor.html', {'form': form})


# =============================================================================
# VISTA: registro_suplidor (DESACTIVADO)
# =============================================================================
# Propósito: Permite a un usuario registrarse como suplidor (intermediario).
# Actualmente desactivado por decisión de ONPECO (ver Fase 41).
#
# URLs asociadas:
#   - /users/registro/suplidor/ (oculto)
#
# Estado: ⛔ DESACTIVADO
# =============================================================================
def registro_suplidor(request):
    """
    Vista para registro de Suplidores (DESACTIVADO)
    """
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        form = RegistroSuplidorForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '✅ ¡Registro exitoso! Tu cuenta ha sido creada y será revisada por ONPECO. Recibirás una notificación cuando sea aprobada.')
            return redirect('users:login')
        else:
            messages.error(request, '❌ Por favor corrige los errores en el formulario.')
    else:
        form = RegistroSuplidorForm()
    
    return render(request, 'users/registro_suplidor.html', {'form': form})


# =============================================================================
# AUTENTICACIÓN
# =============================================================================

# =============================================================================
# VISTA: login_view
# =============================================================================
# Propósito: Permite a los usuarios iniciar sesión con su cédula y contraseña.
# Detecta si el usuario debe cambiar su contraseña temporal.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#
# Retorna:
#   - GET: Renderiza 'users/login.html' con el formulario
#   - POST: Autentica al usuario y redirige al inicio
#
# URLs asociadas:
#   - /users/login/
#
# Flujo de trabajo:
#   1. Verificar que el usuario no esté autenticado
#   2. Procesar POST con cédula y contraseña
#   3. Autenticar usuario
#   4. Verificar si debe cambiar contraseña temporal
#   5. Iniciar sesión y redirigir
# =============================================================================
def login_view(request):
    """
    Vista para iniciar sesión
    """
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Verificar si el usuario debe cambiar su contraseña temporal
            if getattr(user, 'must_change_password', False):
                login(request, user)
                messages.warning(request, '⚠️ Debes cambiar tu contraseña temporal antes de continuar.')
                return redirect('users:cambiar_contrasena_temporal')
            
            login(request, user)
            messages.success(request, f'✅ ¡Bienvenido de vuelta, {username}!')
            return redirect('inicio')
        else:
            messages.error(request, '❌ Usuario o contraseña incorrectos.')
    
    return render(request, 'users/login.html')


# =============================================================================
# VISTA: logout_view
# =============================================================================
# Propósito: Cierra la sesión del usuario actual.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Redirige al inicio
#
# URLs asociadas:
#   - /users/logout/
# =============================================================================
def logout_view(request):
    """
    Vista para cerrar sesión
    """
    logout(request)
    messages.info(request, '📤 Has cerrado sesión exitosamente.')
    return redirect('inicio')


# =============================================================================
# PERFIL DE USUARIO
# =============================================================================

# =============================================================================
# VISTA: perfil
# =============================================================================
# Propósito: Permite al usuario ver y editar su perfil.
# Los campos sensibles (username, first_name, last_name) no son editables.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#
# Retorna:
#   - GET: Renderiza 'users/perfil.html' con los datos del usuario
#   - POST: Actualiza los campos editables y redirige
#
# URLs asociadas:
#   - /users/perfil/
#
# Roles permitidos:
#   - ✅ Todos los usuarios autenticados
#
# Campos editables:
#   - phone: Número de teléfono
#   - address: Dirección
#   - email: Correo electrónico
#   - is_profile_public: Privacidad del perfil
#   - business_name: (solo productores/suplidores)
#   - profile_image: Foto de perfil
#
# Campos protegidos:
#   - username (cédula)
#   - first_name
#   - last_name
# =============================================================================
@login_required
def perfil(request):
    """
    Vista para ver y editar perfil de usuario
    """
    user = request.user
    
    if request.method == 'POST':
        # ============================================================
        # CAMPOS PROTEGIDOS (NO EDITABLES)
        # ============================================================
        # username (cédula), first_name, last_name NO se actualizan
        # Esto evita que los usuarios modifiquen su identidad
        
        # ============================================================
        # CAMPOS EDITABLES
        # ============================================================
        user.phone = request.POST.get('phone', user.phone)
        user.address = request.POST.get('address', user.address)
        user.email = request.POST.get('email', user.email)
        
        # Privacidad del perfil público
        user.is_profile_public = request.POST.get('is_profile_public') == 'on'
        
        # Actualizar rol si el usuario es staff (ONPECO)
        if request.user.is_staff and request.POST.get('role'):
            user.role = request.POST.get('role')
        
        # Nombre del negocio (solo para productores y suplidores)
        if user.role in ['productor', 'suplidor']:
            user.business_name = request.POST.get('business_name', user.business_name)
        
        # Foto de perfil
        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']
        
        user.save()
        messages.success(request, '✅ Perfil actualizado exitosamente.')
        return redirect('users:perfil')
    
    return render(request, 'users/perfil.html', {'user': user})


# =============================================================================
# APROBACIÓN DE PRODUCTORES Y SUPLIDORES (ONPECO)
# =============================================================================

# =============================================================================
# VISTA: lista_productores_pendientes
# =============================================================================
# Propósito: Muestra a ONPECO la lista de productores pendientes y aprobados.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'users/aprobar_productores.html'
#
# URLs asociadas:
#   - /users/aprobar-productores/
#
# Roles permitidos:
#   - ✅ Staff (ONPECO)
#   - ❌ Otros usuarios
# =============================================================================
@staff_member_required
def lista_productores_pendientes(request):
    """
    Vista para que ONPECO vea los productores pendientes de aprobación
    """
    productores_pendientes = User.objects.filter(role='productor', is_approved=False)
    productores_aprobados = User.objects.filter(role='productor', is_approved=True)
    
    context = {
        'pendientes': productores_pendientes,
        'aprobados': productores_aprobados,
    }
    return render(request, 'users/aprobar_productores.html', context)


# =============================================================================
# VISTA: lista_suplidores_pendientes
# =============================================================================
# Propósito: Muestra a ONPECO la lista de suplidores pendientes y aprobados.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'users/aprobar_suplidores.html'
#
# URLs asociadas:
#   - /users/aprobar-suplidores/
#
# Roles permitidos:
#   - ✅ Staff (ONPECO)
# =============================================================================
@staff_member_required
def lista_suplidores_pendientes(request):
    """
    Vista para que ONPECO vea los suplidores pendientes de aprobación
    """
    suplidores_pendientes = User.objects.filter(role='suplidor', is_approved=False)
    suplidores_aprobados = User.objects.filter(role='suplidor', is_approved=True)
    
    context = {
        'pendientes': suplidores_pendientes,
        'aprobados': suplidores_aprobados,
    }
    return render(request, 'users/aprobar_suplidores.html', context)


# =============================================================================
# VISTA: aprobar_productor
# =============================================================================
# Propósito: Aprueba un productor específico (is_approved = True).
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - user_id: ID del productor a aprobar
#
# Retorna:
#   - HttpResponse: Redirige a 'lista_productores_pendientes'
#
# URLs asociadas:
#   - /users/aprobar/<user_id>/
#
# Roles permitidos:
#   - ✅ Staff (ONPECO)
# =============================================================================
@staff_member_required
def aprobar_productor(request, user_id):
    """
    Vista para aprobar un productor específico
    """
    productor = get_object_or_404(User, id=user_id, role='productor')
    productor.is_approved = True
    productor.save()
    
    messages.success(request, f'✅ Productor "{productor.username}" ha sido aprobado exitosamente.')
    return redirect('users:lista_productores_pendientes')


# =============================================================================
# VISTA: rechazar_productor
# =============================================================================
# Propósito: Rechaza un productor específico (is_approved = False).
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - user_id: ID del productor a rechazar
#
# Retorna:
#   - HttpResponse: Redirige a 'lista_productores_pendientes'
#
# URLs asociadas:
#   - /users/rechazar/<user_id>/
#
# Roles permitidos:
#   - ✅ Staff (ONPECO)
# =============================================================================
@staff_member_required
def rechazar_productor(request, user_id):
    """
    Vista para rechazar un productor (opcional)
    """
    productor = get_object_or_404(User, id=user_id, role='productor')
    productor.is_approved = False
    productor.save()
    
    messages.warning(request, f'⚠️ Productor "{productor.username}" ha sido rechazado.')
    return redirect('users:lista_productores_pendientes')


# =============================================================================
# VISTA: aprobar_suplidor
# =============================================================================
# Propósito: Aprueba un suplidor específico (is_approved = True).
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - user_id: ID del suplidor a aprobar
#
# Retorna:
#   - HttpResponse: Redirige a 'lista_suplidores_pendientes'
#
# URLs asociadas:
#   - /users/aprobar-suplidor/<user_id>/
#
# Roles permitidos:
#   - ✅ Staff (ONPECO)
# =============================================================================
@staff_member_required
def aprobar_suplidor(request, user_id):
    """
    Vista para aprobar un suplidor específico
    """
    suplidor = get_object_or_404(User, id=user_id, role='suplidor')
    suplidor.is_approved = True
    suplidor.save()
    
    messages.success(request, f'✅ Suplidor "{suplidor.username}" ha sido aprobado exitosamente.')
    return redirect('users:lista_suplidores_pendientes')


# =============================================================================
# VISTA: rechazar_suplidor
# =============================================================================
# Propósito: Rechaza un suplidor específico (is_approved = False).
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - user_id: ID del suplidor a rechazar
#
# Retorna:
#   - HttpResponse: Redirige a 'lista_suplidores_pendientes'
#
# URLs asociadas:
#   - /users/rechazar-suplidor/<user_id>/
#
# Roles permitidos:
#   - ✅ Staff (ONPECO)
# =============================================================================
@staff_member_required
def rechazar_suplidor(request, user_id):
    """
    Vista para rechazar un suplidor
    """
    suplidor = get_object_or_404(User, id=user_id, role='suplidor')
    suplidor.is_approved = False
    suplidor.save()
    
    messages.warning(request, f'⚠️ Suplidor "{suplidor.username}" ha sido rechazado.')
    return redirect('users:lista_suplidores_pendientes')


# =============================================================================
# PERFIL PÚBLICO DE PRODUCTORES
# =============================================================================

# =============================================================================
# VISTA: perfil_publico_productor
# =============================================================================
# Propósito: Muestra el perfil público de un productor a cualquier visitante.
# Solo visible si el productor tiene is_profile_public = True.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - user_id: ID del productor
#
# Retorna:
#   - HttpResponse: Renderiza 'users/perfil_publico_productor.html'
#
# URLs asociadas:
#   - /users/perfil/<user_id>/
#
# Roles permitidos:
#   - ✅ Todos los visitantes (si el perfil es público)
#   - ✅ Dueño del perfil
#   - ✅ Staff (ONPECO)
#
# Información mostrada:
#   - Nombre del negocio
#   - Nombre real del productor
#   - Calificación promedio
#   - Productos del productor
#   - Reseñas de clientes
# =============================================================================
def perfil_publico_productor(request, user_id):
    """
    Vista pública del perfil del productor
    Solo visible si el productor tiene is_profile_public = True
    """
    from apps.reviews.models import Review
    from django.db.models import Avg
    
    # Buscar productor aprobado
    productor = get_object_or_404(
        User, 
        id=user_id, 
        role='productor',
        is_approved=True
    )
    
    # Verificar si el perfil es público
    if not productor.is_profile_public:
        if not request.user.is_authenticated or (request.user.id != productor.id and not request.user.is_staff):
            raise Http404("Este perfil no está disponible públicamente.")
    
    # Obtener productos del productor
    productos = []
    try:
        from apps.marketplace.models import Product
        productos = Product.objects.filter(vendedor=productor, available=True)[:12]
    except:
        pass
    
    # Calcular calificación desde reseñas
    reseñas = Review.objects.filter(productor=productor)
    total_reseñas = reseñas.count()
    promedio = reseñas.aggregate(avg=Avg('rating'))['avg']
    promedio_calificacion = round(promedio, 1) if promedio else 5.0
    
    context = {
        'productor': productor,
        'productos': productos,
        'promedio_calificacion': promedio_calificacion,
        'total_reseñas': total_reseñas,
    }
    return render(request, 'users/perfil_publico_productor.html', context)


# =============================================================================
# VISTA: lista_productores_publicos
# =============================================================================
# Propósito: Muestra la lista pública de todos los productores aprobados
# con perfil público. Incluye buscador en tiempo real.
#
# Parámetros:
#   - request: Objeto HttpRequest con GET (q)
#
# Retorna:
#   - HttpResponse: Renderiza 'users/lista_productores_publicos.html'
#
# URLs asociadas:
#   - /users/productores/
#
# Roles permitidos:
#   - ✅ Todos los visitantes
#
# Características:
#   - Búsqueda por nombre, negocio, dirección
#   - Muestra calificación promedio
#   - Enlace al perfil público
# =============================================================================
def lista_productores_publicos(request):
    """
    Vista pública que muestra todos los productores con perfil público
    Cualquier visitante puede ver esta lista
    """
    from apps.reviews.models import Review
    from django.db.models import Avg
    
    # Obtener todos los productores aprobados con perfil público
    productores = User.objects.filter(
        role='productor',
        is_approved=True,
        is_profile_public=True
    ).order_by('business_name')
    
    # Buscador
    query = request.GET.get('q', '')
    if query:
        productores = productores.filter(
            models.Q(business_name__icontains=query) |
            models.Q(first_name__icontains=query) |
            models.Q(last_name__icontains=query) |
            models.Q(address__icontains=query)
        )
    
    # Calcular calificación promedio para cada productor
    for productor in productores:
        promedio = Review.objects.filter(productor=productor).aggregate(avg=Avg('rating'))['avg']
        productor.promedio_calificacion = round(promedio, 1) if promedio else 5.0
    
    context = {
        'productores': productores,
        'query': query,
        'total_productores': productores.count(),
    }
    return render(request, 'users/lista_productores_publicos.html', context)


# =============================================================================
# RECUPERACIÓN DE CONTRASEÑA
# =============================================================================

# =============================================================================
# VISTA: CustomPasswordResetView
# =============================================================================
# Propósito: Permite a un usuario solicitar el restablecimiento de su contraseña
# proporcionando su correo electrónico.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#
# Retorna:
#   - GET: Renderiza 'users/password_reset.html'
#   - POST: Envía el correo y redirige a 'password_reset_done'
#
# URLs asociadas:
#   - /users/password-reset/
# =============================================================================
class CustomPasswordResetView(PasswordResetView):
    """Vista para solicitar restablecimiento de contraseña"""
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('users:password_reset_done')
    
    def form_valid(self, form):
        # Guardar el email en la sesión para mostrarlo en la página de confirmación
        self.request.session['reset_email'] = form.cleaned_data['email']
        return super().form_valid(form)


# =============================================================================
# VISTA: CustomPasswordResetDoneView
# =============================================================================
# Propósito: Muestra la confirmación de que el correo fue enviado.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'users/password_reset_done.html'
#
# URLs asociadas:
#   - /users/password-reset/done/
# =============================================================================
class CustomPasswordResetDoneView(PasswordResetDoneView):
    """Vista después de enviar el correo de restablecimiento"""
    template_name = 'users/password_reset_done.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = self.request.session.get('reset_email', '')
        return context


# =============================================================================
# VISTA: CustomPasswordResetConfirmView
# =============================================================================
# Propósito: Permite al usuario establecer una nueva contraseña usando el
# enlace recibido por correo.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - uidb64: ID del usuario codificado
#   - token: Token de seguridad
#
# Retorna:
#   - HttpResponse: Renderiza 'users/password_reset_confirm.html'
#
# URLs asociadas:
#   - /users/password-reset/<uidb64>/<token>/
# =============================================================================
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """Vista para confirmar el restablecimiento de contraseña"""
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


# =============================================================================
# VISTA: CustomPasswordResetCompleteView
# =============================================================================
# Propósito: Muestra la confirmación de que la contraseña fue cambiada.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'users/password_reset_complete.html'
#
# URLs asociadas:
#   - /users/password-reset/complete/
# =============================================================================
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """Vista después de restablecer la contraseña"""
    template_name = 'users/password_reset_complete.html'


# =============================================================================
# GESTIÓN DE USUARIOS POR ONPECO
# =============================================================================

# =============================================================================
# VISTA: lista_usuarios_onpeco
# =============================================================================
# Propósito: Muestra a ONPECO la lista completa de usuarios del sistema
# para gestionar sus contraseñas.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'users/lista_usuarios_onpeco.html'
#
# URLs asociadas:
#   - /users/onpeco/usuarios/
#
# Roles permitidos:
#   - ✅ Staff (ONPECO)
#   - ✅ Regulador (ONPECO)
#
# Características:
#   - Buscador en tiempo real
#   - Botón para restablecer contraseña
# =============================================================================
@login_required
def lista_usuarios_onpeco(request):
    """
    Vista para que ONPECO vea todos los usuarios del sistema
    y pueda gestionar sus contraseñas
    """
    # Verificar que el usuario actual sea ONPECO (staff o regulador)
    if not (request.user.is_staff or getattr(request.user, 'role', '') == 'regulador'):
        return HttpResponseForbidden("No tienes permiso para acceder a esta función.")
    
    # Obtener todos los usuarios ordenados por fecha de registro (más recientes primero)
    usuarios = User.objects.all().order_by('-date_joined')
    
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'users/lista_usuarios_onpeco.html', context)


# =============================================================================
# VISTA: resetear_contrasena_usuario
# =============================================================================
# Propósito: Permite a ONPECO restablecer la contraseña de un usuario a
# 'cambiar123', forzando al usuario a cambiarla al iniciar sesión.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#   - user_id: ID del usuario a restablecer
#
# Retorna:
#   - GET: Renderiza 'users/resetear_contrasena.html'
#   - POST: Restablece la contraseña y redirige a la lista de usuarios
#
# URLs asociadas:
#   - /users/resetear-contrasena/<user_id>/
#
# Roles permitidos:
#   - ✅ Staff (ONPECO)
#   - ✅ Regulador (ONPECO)
#
# Flujo de trabajo:
#   1. Verificar permisos
#   2. No permitir restablecer contraseña de otro administrador
#   3. Establecer contraseña a 'cambiar123'
#   4. Marcar must_change_password = True
#   5. Mostrar mensaje con la contraseña temporal
# =============================================================================
@login_required
def resetear_contrasena_usuario(request, user_id):
    """
    Vista para que ONPECO restablezca la contraseña a 'cambiar123'
    """
    # Verificar que el usuario actual sea ONPECO (staff o regulador)
    if not (request.user.is_staff or getattr(request.user, 'role', '') == 'regulador'):
        return HttpResponseForbidden("No tienes permiso para acceder a esta función.")
    
    usuario = get_object_or_404(User, id=user_id)
    
    # No permitir restablecer contraseña de otro regulador o staff (por seguridad)
    if usuario.is_staff and not request.user.is_superuser:
        messages.error(request, '❌ No puedes restablecer la contraseña de otro administrador.')
        return redirect('users:lista_usuarios_onpeco')
    
    if request.method == 'POST':
        # Contraseña temporal fija
        nueva_contrasena = 'cambiar123'
        
        # Actualizar la contraseña
        usuario.password = make_password(nueva_contrasena)
        usuario.must_change_password = True  # Forzar cambio de contraseña
        usuario.save()
        
        # Mostrar mensaje de confirmación
        messages.success(
            request,
            f'✅ Contraseña restablecida para "{usuario.username}"\n\n'
            f'🔑 <strong style="font-size: 1.5rem; background: #fff3cd; padding: 4px 12px; border-radius: 6px;">cambiar123</strong>\n\n'
            f'📌 <strong>El usuario debe iniciar sesión con "cambiar123" y cambiarla inmediatamente.</strong>'
        )
        return redirect('users:lista_usuarios_onpeco')
    
    context = {
        'usuario': usuario,
    }
    return render(request, 'users/resetear_contrasena.html', context)


# =============================================================================
# VISTA: cambiar_contrasena_temporal
# =============================================================================
# Propósito: Permite a un usuario cambiar su contraseña temporal cuando
# ONPECO la ha restablecido a 'cambiar123'.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#
# Retorna:
#   - GET: Renderiza 'users/cambiar_contrasena_temporal.html'
#   - POST: Cambia la contraseña, cierra sesión y redirige al login
#
# URLs asociadas:
#   - /users/cambiar-contrasena-temporal/
#
# Roles permitidos:
#   - ✅ Usuarios con must_change_password = True
#
# Flujo de trabajo:
#   1. Verificar que el usuario tenga must_change_password = True
#   2. Validar que la nueva contraseña tenga al menos 6 caracteres
#   3. Validar que las contraseñas coincidan
#   4. Guardar la nueva contraseña
#   5. Eliminar la bandera must_change_password
#   6. Cerrar sesión y redirigir al login
# =============================================================================
@login_required
def cambiar_contrasena_temporal(request):
    """
    Vista para que el usuario cambie su contraseña temporal
    """
    user = request.user
    
    # Verificar que el usuario tenga una contraseña temporal
    if not getattr(user, 'must_change_password', False):
        messages.info(request, 'No necesitas cambiar tu contraseña.')
        return redirect('inicio')
    
    if request.method == 'POST':
        nueva = request.POST.get('nueva_contrasena')
        confirmar = request.POST.get('confirmar_contrasena')
        
        if not nueva or len(nueva) < 6:
            messages.error(request, '❌ La contraseña debe tener al menos 6 caracteres.')
            return redirect('users:cambiar_contrasena_temporal')
        
        if nueva != confirmar:
            messages.error(request, '❌ Las contraseñas no coinciden.')
            return redirect('users:cambiar_contrasena_temporal')
        
        # Cambiar la contraseña
        user.password = make_password(nueva)
        user.must_change_password = False
        user.save()
        
        # Forzar logout para que use la nueva contraseña
        logout(request)
        messages.success(request, '✅ Contraseña actualizada exitosamente. ¡Ya puedes usar tu nueva contraseña!')
        messages.info(request, '🔐 Por favor, inicia sesión con tu nueva contraseña.')
        return redirect('users:login')
    
    context = {
        'user': user,
    }
    return render(request, 'users/cambiar_contrasena_temporal.html', context)