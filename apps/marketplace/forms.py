from django import forms
from .models import Product
from apps.users.models import User
from .constants import CATEGORIAS, UNIDADES, SUBCATEGORIAS, get_subcategorias

class ProductoForm(forms.ModelForm):
    """
    Formulario base para crear/editar productos
    Se adapta según el rol del usuario (productor o suplidor)
    """
    
    # Campo de subcategoría (dinámico según la categoría seleccionada)
    subcategory = forms.ChoiceField(
        choices=[], 
        required=True,  # <-- AHORA ES OBLIGATORIO
        label='Subcategoría', 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'subcategory', 'price', 'unit', 'stock', 'stock_minimo', 'image', 'available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Aguacate Hass'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del producto'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'id_category'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad disponible'}),
            'stock_minimo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '5'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Configurar el campo subcategory con las opciones según la categoría actual
        if 'category' in self.data:
            try:
                category = self.data.get('category')
                self.fields['subcategory'].choices = self.get_subcategory_choices(category)
            except:
                pass
        elif self.instance.pk and self.instance.category:
            self.fields['subcategory'].choices = self.get_subcategory_choices(self.instance.category)
            self.fields['subcategory'].initial = self.instance.subcategory
        else:
            self.fields['subcategory'].choices = [('', '--- Selecciona una categoría primero ---')]
        
        # Si el usuario es suplidor, agregamos campos adicionales
        if self.user and self.user.role == 'suplidor':
            self.fields['productor_origen'] = forms.ModelChoiceField(
                queryset=User.objects.filter(role='productor', is_approved=True),
                widget=forms.Select(attrs={'class': 'form-control'}),
                label='Productor original',
                required=True,
                help_text='Selecciona el productor al que le compraste este producto'
            )
            self.fields['precio_compra_productor'] = forms.DecimalField(
                max_digits=10,
                decimal_places=2,
                widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
                label='Precio de compra al productor (RD$)',
                required=True,
                help_text='¿Cuánto pagaste al productor por este producto?'
            )
    
    def get_subcategory_choices(self, category):
        """Retorna las subcategorías disponibles según la categoría principal"""
        
        subcategorias_por_categoria = {
            'frutas': [
                ('citricos', '🍊 Cítricos'),
                ('tropicales', '🥭 Tropicales'),
                ('bayas', '🍓 Bayas'),
                ('otras_frutas', '🍇 Otras frutas'),
            ],
            'verduras': [
                ('hojas_verdes', '🥬 Hojas verdes'),
                ('raices', '🥕 Raíces'),
                ('flores', '🥦 Flores'),
                ('otras_verduras', '🌽 Otras verduras'),
            ],
            'granos': [
                ('arroz', '🍚 Arroz'),
                ('maiz', '🌽 Maíz'),
                ('trigo', '🌾 Trigo'),
                ('avena', '🌾 Avena'),
                ('otros_granos', '📦 Otros granos'),
            ],
            'tuberculos': [
                ('papa', '🥔 Papa'),
                ('yuca', '🌱 Yuca'),
                ('batata', '🍠 Batata'),
                ('name', '🌿 Ñame'),
                ('malanga', '🌿 Malanga'),
                ('otros_tuberculos', '📦 Otros tubérculos'),
            ],
            'legumbres': [
                ('frijoles', '🫘 Frijoles'),
                ('lentejas', '🫘 Lentejas'),
                ('garbanzos', '🫘 Garbanzos'),
                ('habichuelas', '🫘 Habichuelas'),
                ('guandules', '🫘 Guandules'),
                ('otras_legumbres', '📦 Otras legumbres'),
            ],
            'cereal': [
                ('arroz', '🍚 Arroz'),
                ('maiz', '🌽 Maíz'),
                ('trigo', '🌾 Trigo'),
                ('avena', '🌾 Avena'),
                ('cebada', '🌾 Cebada'),
                ('otros_cereales', '📦 Otros cereales'),
            ],
            'lacteos': [
                ('leche', '🥛 Leche'),
                ('queso', '🧀 Queso'),
                ('yogurt', '🫙 Yogurt'),
                ('mantequilla', '🧈 Mantequilla'),
                ('boruga', '🧀 Boruga'),
                ('nata', '🥛 Nata'),
                ('otros_lacteos', '📦 Otros lácteos'),
            ],
            'viveres': [
                ('platano', '🍌 Plátano'),
                ('guineo', '🍌 Guineo'),
                ('relleno', '🍌 Relleno'),
                ('topocho', '🍌 Topocho'),
                ('otros_viveres', '📦 Otros viveres'),
            ],
            'viandas': [
                ('name', '🌿 Ñame'),
                ('malanga', '🌿 Malanga'),
                ('yautia', '🌿 Yautía'),
                ('batata', '🍠 Batata'),
                ('otras_viandas', '📦 Otras viandas'),
            ],
            'bebidas': [
                ('jugos_naturales', '🧃 Jugos naturales'),
                ('refrescos', '🥤 Refrescos'),
                ('agua', '💧 Agua'),
                ('bebidas_lacteas', '🥛 Bebidas lácteas'),
                ('otras_bebidas', '🧃 Otras bebidas'),
            ],
            'condimentos': [
                ('sal', '🧂 Sal'),
                ('pimienta', '🌶️ Pimienta'),
                ('comino', '🌶️ Comino'),
                ('oregano_seco', '🌿 Orégano seco'),
                ('aji', '🌶️ Ají'),
                ('otros_condimentos', '📦 Otros condimentos'),
            ],
            'especias': [
                ('canela', '🌿 Canela'),
                ('clavo', '🌿 Clavo'),
                ('nuez_moscada', '🌿 Nuez moscada'),
                ('jengibre', '🌿 Jengibre'),
                ('curcuma', '🌿 Cúrcuma'),
                ('otras_especias', '📦 Otras especias'),
            ],
            'hierbas_aromaticas': [
                ('cilantro', '🌿 Cilantro'),
                ('perejil', '🌿 Perejil'),
                ('oregano', '🌿 Orégano'),
                ('menta', '🌿 Menta'),
                ('romero', '🌿 Romero'),
                ('albahaca', '🌿 Albahaca'),
                ('otras_hierbas', '🌿 Otras hierbas'),
            ],
            'mariscos': [
                ('camarones', '🦐 Camarones'),
                ('langosta', '🦞 Langosta'),
                ('cangrejo', '🦀 Cangrejo'),
                ('calamar', '🦑 Calamar'),
                ('pulpo', '🐙 Pulpo'),
                ('lambi', '🐚 Lambi'),
                ('vacalao', '🐟 Vacalao'),
                ('otros_mariscos', '📦 Otros mariscos'),
            ],
            'moluscos': [
                ('ostras', '🦪 Ostras'),
                ('mejillones', '🐚 Mejillones'),
                ('almejas', '🐚 Almejas'),
                ('caracoles', '🐚 Caracoles'),
                ('otros_moluscos', '📦 Otros moluscos'),
            ],
            'embutidos_carnes': [
                ('salami', '🥩 Salami'),
                ('jamon', '🥩 Jamón'),
                ('chuletas_con_hueso', '🍖 Chuletas con hueso'),
                ('chuletas_sin_hueso', '🥩 Chuleta sin hueso'),
                ('longaniza', '🌭 Longaniza'),
                ('molida', '🥩 Molida'),
                ('salchichas', '🌭 Salchichas'),
                ('costillitas', '🍖 Costillitas'),
                ('arenque', '🐟 Arenque'),
                ('res', '🥩 Res'),
                ('pollo', '🍗 Pollo'),
                ('cerdo', '🥩 Cerdo'),
                ('pavo', '🦃 Pavo'),
                ('chivo', '🐐 Chivo'),
                ('guineas', '🦃 Guineas'),
                ('otros_embutidos', '📦 Otros embutidos'),
            ],
            'panaderia': [
                ('pan', '🍞 Pan'),
                ('bizcochos', '🎂 Bizcochos'),
                ('pasteles', '🧁 Pasteles'),
                ('reposteria', '🍰 Repostería'),
                ('otros_panaderia', '📦 Otros productos de panadería'),
            ],
            'abarrotes': [
                ('pastas', '🍝 Pastas'),
                ('enlatados', '🥫 Enlatados'),
                ('salsas', '🥫 Salsas'),
                ('vinagres', '🧪 Vinagres'),
                ('otros_abarrotes', '📦 Otros abarrotes'),
            ],
            'cafe_te': [
                ('cafe_grano', '☕ Café en grano'),
                ('cafe_molido', '☕ Café molido'),
                ('te', '🍵 Té'),
                ('infusiones', '🌿 Infusiones'),
                ('otros_cafe_te', '📦 Otros cafés y tés'),
            ],
            'cacao_chocolate': [
                ('cacao_grano', '🍫 Cacao en grano'),
                ('cacao_pasta', '🍫 Pasta de cacao'),
                ('chocolate_artesanal', '🍫 Chocolate artesanal'),
                ('otros_cacao', '📦 Otros productos de cacao'),
            ],
            'hongos_setas': [
                ('champiñones', '🍄 Champiñones'),
                ('portobello', '🍄 Portobello'),
                ('shiitake', '🍄 Shiitake'),
                ('otros_hongos', '📦 Otros hongos'),
            ],
            'pescados': [
                ('pescado_fresco', '🐟 Pescado fresco'),
                ('pescado_salado', '🐟 Pescado salado'),
                ('pescado_ahumado', '🐟 Pescado ahumado'),
                ('otros_pescados', '📦 Otros pescados'),
            ],
            'aceites_grasas': [
                ('aceite_vegetal', '🫒 Aceite vegetal'),
                ('aceite_oliva', '🫒 Aceite de oliva'),
                ('manteca', '🧈 Manteca'),
                ('grasa_cerdo', '🥓 Grasa de cerdo'),
                ('otros_aceites', '📦 Otros aceites y grasas'),
            ],
            'endulzantes': [
                ('azucar', '🍬 Azúcar'),
                ('panela', '🍯 Panela'),
                ('miel', '🍯 Miel de abeja'),
                ('otros_endulzantes', '📦 Otros endulzantes'),
            ],
        }
        # Si la categoría no existe, devolver lista vacía
        return subcategorias_por_categoria.get(category, [])
    
    def clean(self):
        """Validaciones personalizadas del formulario"""
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        
        # ========== VALIDACIÓN: SUBCATEGORÍA OBLIGATORIA ==========
        if not subcategory:
            self.add_error('subcategory', '⚠️ La subcategoría es obligatoria. Selecciona una subcategoría para tu producto.')
            return cleaned_data
        # ========== FIN VALIDACIÓN ==========
        
        # ========== VALIDACIÓN: SUBCATEGORÍA DEBE PERTENECER A LA CATEGORÍA ==========
        subcategorias_validas = [s[0] for s in self.get_subcategory_choices(category)]
        
        if subcategory not in subcategorias_validas:
            self.add_error(
                'subcategory',
                f'⚠️ La subcategoría seleccionada no corresponde a la categoría "{dict(CATEGORIAS).get(category, category)}". '
                f'Selecciona una subcategoría válida para esta categoría.'
            )
            return cleaned_data
        # ========== FIN VALIDACIÓN ==========
        
        # ========== VALIDACIÓN: PRECIO DE VENTA MAYOR A PRECIO DE COMPRA (SUPLIDORES) ==========
        if self.user and self.user.role == 'suplidor':
            precio_compra = cleaned_data.get('precio_compra_productor')
            precio_venta = cleaned_data.get('price')
            
            if precio_compra and precio_venta:
                if precio_compra >= precio_venta:
                    self.add_error(
                        'price',
                        '⚠️ El precio de venta debe ser mayor al precio de compra al productor. '
                        'No se permite vender a pérdida o al costo.'
                    )
        # ========== FIN VALIDACIÓN ==========
        
        return cleaned_data

    def save(self, commit=True):
        producto = super().save(commit=False)
        producto.vendedor = self.user
        
        # Guardar subcategoría
        producto.subcategory = self.cleaned_data.get('subcategory')
        
        if self.user and self.user.role == 'suplidor':
            producto.productor_origen = self.cleaned_data.get('productor_origen')
            producto.precio_compra_productor = self.cleaned_data.get('precio_compra_productor')
        
        if commit:
            producto.save()
        return producto