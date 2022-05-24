from re import template
from django.views.generic import TemplateView
# Create your views here.

home = TemplateView.as_view(template_name="index.html")
tarjeta = TemplateView.as_view(template_name="tarjeta.html")
login = TemplateView.as_view(template_name="login.html")
categoriaperro = TemplateView.as_view(template_name="cat_perro.html")
categoriagato = TemplateView.as_view(template_name="cat_gato.html")