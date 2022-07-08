from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('tarjeta/', views.tarjeta, name="tarjeta"),
    path('login/', views.pagina_login, name="login"),
    path('registro/', views.pagina_registro, name="registro"),
    path('categoria-perro/', views.lista_perros, name="categoriaperro"),
    path('categoria-gato/', views.categoriagato, name="categoriagato"),
    path('productos_crud', views.listar_productos, name="crud"),
    path('crear_producto/', views.crear_producto, name="crear_producto"),
    path('guardar_producto', views.guardar_producto, name="guardar_producto"),
    path('borrar_producto/<int:id>', views.borrar_producto, name="borrar_producto"),
    path('producto/<int:id>', views.ver_producto, name="producto"),
    path('producto/editar/<int:id>', views.editar_producto, name="editar"),
    path('Productos/', views.Productos, name="Productos"),
    path('producto/editar/guardar/<int:id>', views.guardar_edicion, name="guardar_edicion"),
    #path('oauth/', include('social_django.urls', namespace='social')),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)