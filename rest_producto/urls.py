from django.urls import path
from rest_producto.views import lista_producto, detalle_producto, listarProductos, crearProductos, verProductos


urlpatterns = [
##API JSON
    path('lista_producto', lista_producto, name="lista_producto"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
##API Views
    path('', listarProductos, name="listarProductos"),
    path('crear_productos', crearProductos, name="crearProductos"),
    path('ver_producto/<id>', verProductos, name="verProductos"),

]
