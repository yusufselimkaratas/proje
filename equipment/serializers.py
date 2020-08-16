from rest_framework import serializers
from .models import *

class CramponSerializer (serializers.ModelSerializer):
    class Meta:
        model = Crampon
        fields = '__all__'
class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        model= Short
        fields = '__all__'

class ShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model= Shirt
        fields = '__all__'

class EquipmntSerializer(serializers.ModelSerializer):
    class Meta:
        model= Equipment
        fields = '__all__'