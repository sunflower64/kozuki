from re import template
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse, redirect

from web.models import Producto
# Create your views here.

home = TemplateView.as_view(template_name="index.html")
tarjeta = TemplateView.as_view(template_name="tarjeta.html")
login = TemplateView.as_view(template_name="login.html")
categoriaperro = TemplateView.as_view(template_name="cat_perro.html")
categoriagato = TemplateView.as_view(template_name="cat_gato.html")
#CRUD
crud = TemplateView.as_view(template_name='productos_crud.html')
crear_producto = TemplateView.as_view(template_name="crear_producto.html")
ver_producto = TemplateView.as_view(template_name="producto.html")
editar_producto = TemplateView.as_view(template_name="editar.html")

def guardar_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST['nombre_producto']
        marca_producto = request.POST['marca_producto']
        precio_producto = request.POST['precio_producto']
        stock_producto = request.POST['stock_producto']
        descripcion_producto = request.POST['descripcion_producto']

        producto = Producto(
        nombre_producto = nombre_producto,
        marca_producto = marca_producto,
        precio_producto = precio_producto,
        stock_producto = precio_producto,
        descripcion_producto = descripcion_producto,
                )
        producto.save()
        return redirect('crud')
    else:
        HttpResponse('<h2>No se pudo agregar el producto</h2>')

def borrar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    producto.delete()

    return redirect('crud')
def listar_productos(request):
    productos = Producto.objects.all()

    return render(request, 'productos_crud.html' ,{
    'productos': productos
        })

def ver_producto(request, id):
    producto = Producto.objects.get(pk=id)

    return render(request, 'producto.html',{
        'producto': producto
        })

def editar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    return render(request, 'editar.html',{
        'producto': producto
        })

def guardar_edicion(request,id):
    producto = Producto.objects.get(pk=id)
    if request.method == 'POST':
        nombre_producto = request.POST['nombre_producto']
        marca_producto = request.POST['marca_producto']
        precio_producto = request.POST['precio_producto']
        stock_producto = request.POST['stock_producto']
        descripcion_producto = request.POST['descripcion_producto']

        producto = Producto(
        id = id,
        nombre_producto = nombre_producto,
        marca_producto = marca_producto,
        precio_producto = precio_producto,
        stock_producto = precio_producto,
        descripcion_producto = descripcion_producto,
                )
        producto.save()
        return redirect('crud')
    else:
        HttpResponse('<h2>No se pudo agregar los cambios</h2>')

