# En tu archivo mi_app/admin.py

from django.contrib import admin
from .models import Producto, ColorVariante

# Usamos TabularInline para gestionar las variantes de color
# en la misma página de edición de un producto.
class ColorVarianteInline(admin.TabularInline):
    model = ColorVariante
    extra = 1  # Muestra un formulario vacío adicional para agregar una nueva variante

# Creamos una clase personalizada para el modelo Producto
class ProductoAdmin(admin.ModelAdmin):
    # La lista de campos que quieres mostrar en la vista de lista de productos
    list_display = ('nombre', 'categoria', 'precio', 'total_stock')
    # Filtros para la barra lateral
    list_filter = ('categoria', 'color_principal')
    # Campos de búsqueda
    search_fields = ['nombre', 'descripcion']
    # Añadimos el TabularInline que acabamos de crear
    inlines = [ColorVarianteInline]

# Registramos tus modelos en el panel de administración
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ColorVariante)