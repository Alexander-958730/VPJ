from django.shortcuts import redirect
from django.urls import reverse

class BlockAdminForOnpeco:
    """Bloquea el acceso al admin de Django para usuarios ONPECO reguladores"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Si la URL empieza con /admin/
        if request.path.startswith('/admin/'):
            # Si el usuario está autenticado y es regulador (pero no superusuario)
            if request.user.is_authenticated:
                # Si es ONPECO regulador pero NO es superusuario
                if not request.user.is_superuser and getattr(request.user, 'role', '') == 'regulador':
                    return redirect('/denuncias/portal/')
        
        response = self.get_response(request)
        return response