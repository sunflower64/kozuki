from django.db import models

# Create your models here.

class Xao(models.Model):
        id_pepe= models.IntegerField(primary_key=True, verbose_name='ide de los pepes')
        nombre = models.CharField( max_length=30, verbose_name='Nombre_pepes')
        elpepe = models.CharField(max_length=2, verbose_name='el pepex')

        def __str__(self):
            return self.nombre # el dato visible que se muestra en la tabla 



class Usuario(models.Model):
    id_usr  = models.IntegerField(primary_key=True, verbose_name='Id Usuario')
    nombre_usr= models.CharField( max_length=15, verbose_name='Nombre Usuario')
    apellido_usr= models.CharField( max_length=15, verbose_name='Apellido Usuario')
    email_usr = models.CharField( max_length=25, verbose_name='Email Usuario')
    contraseña_usr = models.CharField( max_length=15, verbose_name='Contraseña Usuario')

    def __str__(self):
        return self.id_usr


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombre_categoria = models.CharField(max_length=20, verbose_name='Categoria Producto')
    
    def __str__(self):
        return self.nombre_categoria
    

class Producto(models.Model):
    codigo_prod = models.IntegerField(primary_key=True, verbose_name='Id Producto')
    nombre_prod = models.CharField( max_length=15, verbose_name='Nombre Producto')
    marca_prod = models.CharField( max_length=15, verbose_name='Nombre marca producto')
    precio_prod = models.IntegerField(verbose_name='Precio Producto')
    calificacion = models.IntegerField(blank=True, null=True,  verbose_name='Nota Producto')
    ###
    nombre_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_prod
    

class Promocion(models.Model):
    id_promo = models.IntegerField(primary_key=True, verbose_name='Id Promocion')
    titulo_promo =  models.CharField(max_length=30, verbose_name='Titulo Promocion')
    fecha_inicio = models.DateField(verbose_name='Inicio Promocion')
    fecha_termino = models.DateField(verbose_name='Termino Promocion')
    porc_descuento = models.FloatField(verbose_name='Porcentaje descuento')
###
    codigo_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_promo
    

    