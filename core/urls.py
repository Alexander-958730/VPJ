from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('productos/', include('apps.marketplace.urls')),
    path('denuncias/', include('apps.complaints.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path('export/', include('apps.export.urls')),
    path('', views.inicio, name='inicio'),
    path('chat/', include('apps.chat.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('cart/', include('apps.cart.urls')),
]

# Servir archivos estáticos y media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)