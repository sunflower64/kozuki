from email import message
from functools import reduce
from pkgutil import get_data
from re import template
import re
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from .forms import FormProducto, FormRegistro
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 




from web.models import Producto
# Create your views here.

home = TemplateView.as_view(template_name="index.html")
tarjeta = TemplateView.as_view(template_name="tarjeta.html")
Productos = TemplateView.as_view(template_name="principal_productos.html")
#login = TemplateView.as_view(template_name="login.html")
categoriaperro = TemplateView.as_view(template_name="cat_perro.html")
categoriagato = TemplateView.as_view(template_name="cat_gato.html")
#CRUD
crud = TemplateView.as_view(template_name='productos_crud.html')
#crear_producto = TemplateView.as_view(template_name="crear_producto.html")
ver_producto = TemplateView.as_view(template_name="producto.html")
editar_producto = TemplateView.as_view(template_name="editar.html")

@staff_member_required

def crear_producto(request):

    if request.method == 'POST':
        formulario = FormProducto(request.POST, request.FILES)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            nombre_producto = data_form['nombre_producto']
            marca_producto = data_form['marca_producto']
            tipoanimal_producto = data_form['tipoanimal_producto']
            descripcion_producto = data_form['descripcion_producto']
            precio_producto = data_form['precio_producto']
            stock_producto = data_form['stock_producto']
            foto_producto = data_form['foto_producto']

            producto = Producto(
            nombre_producto = nombre_producto,
            marca_producto = marca_producto,
            tipoanimal_producto = tipoanimal_producto,
            descripcion_producto = descripcion_producto,
            precio_producto = precio_producto,
            stock_producto = precio_producto,
            foto_producto = foto_producto,
                    )
            producto.save()

            return redirect('crud')
    else:
        formulario = FormProducto()
    return render(request, "crear_producto.html", {
        'form': formulario
    })

def guardar_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST['nombre_producto']
        marca_producto = request.POST['marca_producto']
        tipoanimal_producto = request.POST['tipoanimal_producto']
        descripcion_producto = request.POST['descripcion_producto']
        precio_producto = request.POST['precio_producto']
        stock_producto = request.POST['stock_producto']
        foto_producto = request.FILES.POST['foto_producto']
        

        producto = Producto(
        nombre_producto = nombre_producto,
        marca_producto = marca_producto,
        tipoanimal_producto = tipoanimal_producto,
        descripcion_producto = descripcion_producto,
        precio_producto = precio_producto,
        stock_producto = precio_producto,
        foto_producto = foto_producto,
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

def pagina_registro(request):
    
    form_registro = FormRegistro()

    if request.method == 'POST':
       form_registro = FormRegistro(request.POST)

       if form_registro.is_valid():
        form_registro.save()

        return redirect('home')
    
    return render(request, 'usuarios/registro.html', {
        'form_registro': form_registro
    })

def pagina_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('crud')
        else:
            HttpResponse('<h2>No te identificaste correctamente</h2>')
    else:
            HttpResponse('<h2>Necesito dormir/h2>')

    return render(request, 'usuarios/login.html')

def lista_perros(request):
    productos = Producto.objects.filter(tipoanimal_producto=1)
    return render(request, 'cat_perro.html' ,{
    'productos': productos
        })