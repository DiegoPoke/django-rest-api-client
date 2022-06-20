from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Client
from .serializers import ClienteSerializer
from rest_framework import permissions

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]