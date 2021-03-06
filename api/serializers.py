#from dataclasses import field
from rest_framework import routers, serializers, viewsets
from .models import Client

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','name', 'bdate', 'address', 'zipcode']
