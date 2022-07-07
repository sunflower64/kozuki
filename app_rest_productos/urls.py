from django.urls import path
from app_rest_productos.views import api_traer_productos, api_ver_producto

urlpatterns = [
    path('', api_traer_productos, name="api_traer_productos"),
    path('ver_producto/<id>', api_ver_producto, name="api_ver_producto"),

    ]
