from dataclasses import fields
from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormProducto(forms.Form):
    nombre_producto = forms.CharField(
        label = "Titulo",
    )
    marca_producto = forms.CharField()
    tipoanimal_producto_opciones = [
        (0, 'Gato'),
        (1, 'Perro'),
        (2, 'Ambos')

    ]
    tipoanimal_producto = forms.TypedChoiceField(
        choices = tipoanimal_producto_opciones
    )
    descripcion_producto = forms.CharField()
    precio_producto = forms.IntegerField()
    stock_producto = forms.IntegerField()
    foto_producto = forms.ImageField()

class FormRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']