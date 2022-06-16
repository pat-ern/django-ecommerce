from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Producto
from .serializers import ProductoSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    #discriminar si es GET o POST
    if request.method == 'GET':
        productos = Producto.objects.all().order_by('id')
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_producto(request, nombre):

    try: # se busca producto por nombre
        producto = Producto.objects.get(nombre=nombre)
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': #se obtienen datos de UN producto por nombre
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    if request.method == 'PUT': #se actualizan datos de UN producto por nombre
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data = data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE': #elimino 1 producto por su nombre
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)