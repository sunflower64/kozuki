from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=15)

class Promocion(models.Model):
    titulo_promocion = models.CharField(max_length=30)
    descripcion_promocion = models.CharField(max_length=50)
    inicio_promocion = models.DateField()
    termino_promocion = models.DateField()
    descuento_promocion = models.IntegerField()

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    marca_producto = models.CharField(max_length=25)
    tipoanimal_producto = models.IntegerField(null=True)
    descripcion_producto = models.CharField(max_length=300)
    precio_producto = models.IntegerField()
    stock_producto = models.IntegerField()
    foto_producto = models.ImageField(upload_to="productos/", null=True, blank=True)
#    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
