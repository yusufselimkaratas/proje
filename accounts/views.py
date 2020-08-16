from django.shortcuts import render

# Create your views here.

from .serializers import *
from rest_framework import viewsets

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class =  CustomerSerializer


class FieldOwnerViewSet(viewsets.ModelViewSet):
    queryset = FieldOwner.objects.all()
    serializer_class = FieldOwnerSerializer

# TODO: FieldOwner create should not require user information

class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
