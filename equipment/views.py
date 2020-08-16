from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class CramponViewSet(viewsets.ModelViewSet):
    queryset = Crampon.objects.all()
    serializer_class = CramponSerializer

class ShortViewSet(viewsets.ModelViewSet):
    queryset = Short.objects.all()
    serializer_class = ShortSerializer

class ShirtViewSet(viewsets.ModelViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmntSerializer