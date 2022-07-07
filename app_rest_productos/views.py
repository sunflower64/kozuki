from django.shortcuts import render
from web.models import Producto
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductoSerializer

# Create your views here.
# api listar productos + carrito de compras
@csrf_exempt
@api_view(['GET'])
def api_traer_productos(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def api_ver_producto(request, id):
    try:
        producto = Producto.objects.get(id=id)

    except Producto.doesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

