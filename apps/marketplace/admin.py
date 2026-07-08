from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from django.db.models import Count, Sum
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendedor', 'tipo_vendedor', 'productor_origen', 'price', 'stock', 'available')
    list_filter = ('category', 'available', 'vendedor__role')
    search_fields = ('name', 'vendedor__username', 'productor_origen__username')
    
    def tipo_vendedor(self, obj):
        return obj.vendedor.get_role_display() if obj.vendedor else 'N/A'
    tipo_vendedor.short_description = 'Tipo de Vendedor'
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('datos-productos/', self.admin_site.admin_view(self.datos_productos), name='productos_data'),
            path('estadisticas/', self.admin_site.admin_view(self.estadisticas_view), name='productos_estadisticas'),
        ]
        return custom_urls + urls
    
    def datos_productos(self, request):
        """API para obtener estadísticas básicas de productos"""
        total = self.model.objects.count()
        disponibles = self.model.objects.filter(available=True).count()
        no_disponibles = self.model.objects.filter(available=False).count()
        
        # Productos por categoría
        por_categoria = list(
            self.model.objects
            .values('category')
            .annotate(count=Count('id'))
            .order_by('-count')
        )
        
        # Productos por tipo de vendedor
        por_tipo_vendedor = list(
            self.model.objects
            .values('vendedor__role')
            .annotate(count=Count('id'))
            .order_by('-count')
        )
        
        # Precio promedio
        precio_promedio = self.model.objects.aggregate(promedio=Sum('price') / Count('id'))['promedio'] or 0
        
        return JsonResponse({
            'total': total,
            'disponibles': disponibles,
            'no_disponibles': no_disponibles,
            'por_categoria': por_categoria,
            'por_tipo_vendedor': por_tipo_vendedor,
            'precio_promedio': round(precio_promedio, 2),
        })
    
    def estadisticas_view(self, request):
        """Vista para mostrar gráficos de productos"""
        from django.shortcuts import render
        context = dict(
            self.admin_site.each_context(request),
            title="Estadísticas de Productos",
        )
        return render(request, "admin/marketplace/estadisticas.html", context)

admin.site.register(Product, ProductAdmin)