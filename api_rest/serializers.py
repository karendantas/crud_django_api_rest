from rest_framework import serializers
from .models import User

#Serializers convertem models para o formato JSON

class UserSerializer(serializers.ModelSerializer):
    #aqui defini-se qual o model e quais campos deste serão convetidos em JSON
    class Meta:
        model = User
        fields = '__all__'