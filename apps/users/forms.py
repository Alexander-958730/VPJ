from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import authenticate
from .models import User
import re

# ====================== FUNCIÓN DE VALIDACIÓN DE CÉDULA ======================

def validar_cedula_rd(cedula):
    """
    Valida el número de cédula de República Dominicana.
    Algoritmo oficial de la JCE.
    
    Proceso:
    1. Multiplicar dígitos en posiciones impares por 1 y pares por 2
    2. Sumar los dígitos de los resultados
    3. El dígito verificador = 10 - (suma % 10)
    """
    # Limpiar la cédula (quitar guiones y espacios)
    cedula = re.sub(r'[\s-]', '', cedula)
    
    # Verificar que sean 11 dígitos
    if not cedula.isdigit() or len(cedula) != 11:
        return False
    
    # Extraer el dígito verificador (último dígito)
    digito_verificador = int(cedula[10])
    
    # Procesar los primeros 10 dígitos (de izquierda a derecha)
    suma = 0
    
    for i in range(10):
        digito = int(cedula[i])
        posicion = i + 1  # Posición comenzando desde 1
        
        # Posiciones impares: multiplicar por 1
        # Posiciones pares: multiplicar por 2
        if posicion % 2 != 0:  # Posición impar
            resultado = digito * 1
            suma += resultado
        else:  # Posición par
            resultado = digito * 2
            # Si el resultado es mayor o igual a 10, sumar los dígitos
            if resultado >= 10:
                resultado = (resultado // 10) + (resultado % 10)
            suma += resultado
    
    # Calcular el dígito verificador esperado
    residuo = suma % 10
    digito_esperado = 10 - residuo
    
    # Comparar con el dígito verificador real
    return digito_verificador == digito_esperado


def formatear_cedula(cedula):
    """Formatea la cédula como 001-1234567-8"""
    cedula = re.sub(r'[\s-]', '', cedula)
    if len(cedula) == 11:
        return f"{cedula[:3]}-{cedula[3:10]}-{cedula[10]}"
    return cedula


def limpiar_cedula(cedula):
    """Elimina guiones y espacios de la cédula"""
    return re.sub(r'[\s-]', '', cedula)


# ====================== FORMULARIO DE AUTENTICACIÓN PERSONALIZADO ======================

class CustomAuthenticationForm(forms.Form):
    """Formulario personalizado para autenticación que acepta cédula con o sin guiones"""
    username = forms.CharField(
        max_length=150,
        label='Número de Cédula',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': '001-1234567-8 o 00112345678',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Eliminar guiones y espacios para buscar en la base de datos
        username_clean = re.sub(r'[\s-]', '', username)
        
        # Verificar si existe un usuario con ese nombre de usuario (sin guiones)
        try:
            user = User.objects.get(username=username_clean)
            return user.username  # Devolver el username guardado (sin guiones)
        except User.DoesNotExist:
            raise forms.ValidationError('⚠️ Usuario no encontrado. Verifica tu número de cédula.')
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            # Autenticar al usuario
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('⚠️ Usuario o contraseña incorrectos.')
            cleaned_data['user'] = user
        return cleaned_data


# ====================== FORMULARIOS DE REGISTRO ======================

class RegistroConsumidorForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'})
    )
    phone = forms.CharField(
        max_length=15, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '809-555-1234'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Calle, número, sector'}), 
        required=False
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '001-1234567-8 o 00112345678',
                'title': 'Ingresa tu cédula con o sin guiones'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Número de Cédula'
        self.fields['username'].help_text = 'Ingresa tu cédula con o sin guiones (ej: 001-1234567-8 o 00112345678)'
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mínimo 8 caracteres'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Repite la contraseña'})
    
    def clean_username(self):
        """Valida que el nombre de usuario sea una cédula válida y no esté duplicada"""
        username = self.cleaned_data.get('username')
        
        # Eliminar guiones y espacios para validar
        username_clean = limpiar_cedula(username)
        
        # Validar formato de cédula
        if not validar_cedula_rd(username_clean):
            raise forms.ValidationError(
                '⚠️ Número de cédula inválido. Verifica que sean 11 dígitos y que el dígito verificador sea correcto.'
            )
        
        # Verificar que no esté duplicada
        if User.objects.filter(username=username_clean).exists():
            raise forms.ValidationError('⚠️ Este número de cédula ya está registrado. Por favor verifica.')
        
        # Guardar sin guiones
        return username_clean
    
    def clean_email(self):
        """Valida que el correo electrónico no esté duplicado"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('⚠️ Este correo electrónico ya está registrado. Por favor usa otro.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        user.role = 'consumidor'
        user.is_approved = True
        if commit:
            user.save()
        return user


class RegistroProductorForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'})
    )
    phone = forms.CharField(
        max_length=15, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '809-555-1234'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Calle, número, sector'}), 
        required=True
    )
    business_name = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tu finca o negocio'})
    )
    
    # ========== NUEVOS CAMPOS: NOMBRE Y APELLIDO ==========
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan'}),
        label='Nombre del dueño/representante'
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Pérez'}),
        label='Apellido del dueño/representante'
    )
    # ========== FIN NUEVOS CAMPOS ==========
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address', 'business_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '001-1234567-8 o 00112345678',
                'title': 'Ingresa tu cédula con o sin guiones'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Número de Cédula'
        self.fields['username'].help_text = 'Ingresa tu cédula con o sin guiones (ej: 001-1234567-8 o 00112345678)'
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mínimo 8 caracteres'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Repite la contraseña'})
    
    def clean_username(self):
        """Valida que el nombre de usuario sea una cédula válida y no esté duplicada"""
        username = self.cleaned_data.get('username')
        
        # Eliminar guiones y espacios para validar
        username_clean = limpiar_cedula(username)
        
        # Validar formato de cédula
        if not validar_cedula_rd(username_clean):
            raise forms.ValidationError(
                '⚠️ Número de cédula inválido. Verifica que sean 11 dígitos y que el dígito verificador sea correcto.'
            )
        
        # Verificar que no esté duplicada
        if User.objects.filter(username=username_clean).exists():
            raise forms.ValidationError('⚠️ Este número de cédula ya está registrado. Por favor verifica.')
        
        # Guardar sin guiones
        return username_clean
    
    def clean_email(self):
        """Valida que el correo electrónico no esté duplicado"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('⚠️ Este correo electrónico ya está registrado. Por favor usa otro.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        user.business_name = self.cleaned_data['business_name']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.role = 'productor'
        user.is_approved = False
        if commit:
            user.save()
        return user


class RegistroSuplidorForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'})
    )
    phone = forms.CharField(
        max_length=15, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '809-555-1234'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Calle, número, sector'}), 
        required=True
    )
    business_name = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tu empresa o negocio'})
    )
    
    # ========== NUEVOS CAMPOS: NOMBRE Y APELLIDO ==========
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan'}),
        label='Nombre del dueño/representante'
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Pérez'}),
        label='Apellido del dueño/representante'
    )
    # ========== FIN NUEVOS CAMPOS ==========
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address', 'business_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '001-1234567-8 o 00112345678',
                'title': 'Ingresa tu cédula con o sin guiones'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Número de Cédula'
        self.fields['username'].help_text = 'Ingresa tu cédula con o sin guiones (ej: 001-1234567-8 o 00112345678)'
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mínimo 8 caracteres'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Repite la contraseña'})
    
    def clean_username(self):
        """Valida que el nombre de usuario sea una cédula válida y no esté duplicada"""
        username = self.cleaned_data.get('username')
        
        # Eliminar guiones y espacios para validar
        username_clean = limpiar_cedula(username)
        
        # Validar formato de cédula
        if not validar_cedula_rd(username_clean):
            raise forms.ValidationError(
                '⚠️ Número de cédula inválido. Verifica que sean 11 dígitos y que el dígito verificador sea correcto.'
            )
        
        # Verificar que no esté duplicada
        if User.objects.filter(username=username_clean).exists():
            raise forms.ValidationError('⚠️ Este número de cédula ya está registrado. Por favor verifica.')
        
        # Guardar sin guiones
        return username_clean
    
    def clean_email(self):
        """Valida que el correo electrónico no esté duplicado"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('⚠️ Este correo electrónico ya está registrado. Por favor usa otro.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        user.business_name = self.cleaned_data['business_name']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.role = 'suplidor'
        user.is_approved = False
        if commit:
            user.save()
        return user


# ====================== FORMULARIO PARA RESTABLECER CONTRASEÑA ======================

class CustomPasswordResetForm(PasswordResetForm):
    """Formulario personalizado para restablecer contraseña"""
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("❌ No existe ninguna cuenta con este correo electrónico.")
        return email