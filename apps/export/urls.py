# apps/export/urls.py
from django.urls import path
from . import views

app_name = 'export'

urlpatterns = [
    path('panel/', views.panel_exportaciones, name='panel'),
    path('denuncias/excel/', views.exportar_denuncias_excel, name='denuncias-excel'),
    path('denuncias/pdf/', views.exportar_denuncias_pdf, name='denuncias-pdf'),
    path('productores/pdf/', views.exportar_productores_pdf, name='productores-pdf'),
]