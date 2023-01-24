
# Create your views here.
from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Planta
from .serializers import PlantaSerializer
from rest_planta import serializers

@csrf_exempt
@api_view(['GET','POST'])
def lista_plantas (request):
    if request.method == 'GET':
        planta = Planta.objects.all()
        serializer = PlantaSerializer(planta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlantaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get update y delete de una planta en particular 

@api_view(['GET','PUT','DELETE'])
def detalle_planta(request, id):

    try:
        planta = Planta.objects.get(id=id)
    except Planta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PlantaSerializer(planta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PlantaSerializer(planta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        planta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


