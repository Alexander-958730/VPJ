from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('calificar/<int:productor_id>/', views.calificar_productor, name='calificar_productor'),
]