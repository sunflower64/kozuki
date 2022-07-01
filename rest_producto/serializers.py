from rest_framework import serializers
from web.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields= "__all__"
        # o tambien fields="__all__" para todos los campos de una
