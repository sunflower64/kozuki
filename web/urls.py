from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tarjeta/', views.tarjeta, name="tarjeta"),
    path('login/', views.login, name="login"),
    path('categoria-perro/', views.categoriaperro, name="categoriaperro"),
    path('categoria-gato/', views.categoriagato, name="categoriagato"),
    path('productos_crud', views.listar_productos, name="crud"),
    path('crear_producto/', views.crear_producto, name="crear_producto"),
    path('guardar_producto', views.guardar_producto, name="guardar_producto"),
    path('borrar_producto/<int:id>', views.borrar_producto, name="borrar_producto"),
    path('producto/<int:id>', views.ver_producto, name="producto"),
    path('producto/editar/<int:id>', views.editar_producto, name="editar"),
    path('producto/editar/guardar/<int:id>', views.guardar_edicion, name="guardar_edicion"),




    path('Productos/', views.productos, name="productos"),

    ]
