from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tarjeta/', views.tarjeta, name="tarjeta"),
    path('login/', views.login, name="login"),
    path('categoria-perro/', views.categoriaperro, name="categoriaperro"),
    path('categoria-gato/', views.categoriagato, name="categoriagato"),
]