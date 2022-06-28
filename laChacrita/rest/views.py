from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Suscripcion
from .serializers import SuscripcionSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# API SUSCRIPCIONES

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_suscripcion(request):
    #discriminar si es GET o POST
    if request.method == 'GET':
        suscripciones = Suscripcion.objects.all().order_by('-id')
        serializer = SuscripcionSerializer(suscripciones, many = True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=SuscripcionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_suscripcion(request, id):

    try: # se busca producto por id
        suscripcion = Suscripcion.objects.get(id=id)
    except Suscripcion.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': #se obtienen datos de UN producto por id
        serializer = SuscripcionSerializer(suscripcion)
        return Response(serializer.data)
    
    if request.method == 'PUT': #se actualizan datos de UN producto por id
        data = JSONParser().parse(request)
        serializer = SuscripcionSerializer(suscripcion, data = data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE': #elimino 1 producto por su id
        suscripcion.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)