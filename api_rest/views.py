from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json
# Create your views here.

#com o decorator, a função so aceita requisições do tipo GET
@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':
        #captura todos os objetos no banco de dados e cria um queryset
        users = User.objects.all()

        #o serializier retorna um JSON. Many=True pois se trata de um queryset
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_by_nickname(request, nickname):
    try:
        user = User.objects.get(pk=nickname)
    except:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)