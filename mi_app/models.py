from django.db import models

class Producto(models.Model):
    COLORES_CHOICES = [
        ('red', 'Rojo'),
        ('blue', 'Azul'),
        ('black', 'Negro'),
        ('white', 'Blanco'),
        ('pink', 'Rosa'),
        ('purple', 'Púrpura'),
    ]
    CATEGORIAS_CHOICES = [
        ('mallas_enterizas', 'Mallas enterizas'),
        ('lenceria', 'Lencería'),
        ('disfraz_sexi', 'Disfraz sexi'),
    ]
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_CHOICES, default='lenceria')
    color_principal = models.CharField(max_length=50, choices=COLORES_CHOICES, default='red')
    imagen_principal = models.ImageField(upload_to='productos/', blank=True, null=True)

    @property
    def total_stock(self):
        return sum(variant.stock for variant in self.variantes.all())

    def __str__(self):
        return self.nombre

class ColorVariante(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='variantes')
    color = models.CharField(max_length=50, choices=Producto.COLORES_CHOICES)
    imagen = models.ImageField(upload_to='productos/')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} - {self.color}"
