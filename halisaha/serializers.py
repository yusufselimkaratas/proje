from rest_framework import serializers

from .models import *

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address

        exclude = ('user',)
class FieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class FieldCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        exclude = ('owner',)

class FieldConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldConfiguration
        fields = '__all__'

class FieldOwnerDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOwnerDiscount
        fields = '__all__'

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'

class PlayerSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSearch
        fields = '__all__'