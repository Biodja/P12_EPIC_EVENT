from asyncio import Event
from django.test import Client
from rest_framework import serializers

from Epic_event.event.models import Contract, Profil, UserType

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', 'type']

class ProfilSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(many=False, read_only=True)
    class Meta:
        model = Profil
        fields = ['id', 'user', 'user_type']

class ClientSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(many=False, read_only=True)
    class Meta:
        model = Client
        fields = ['id', 'user', 'user_type']

class ContractSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(many=False, read_only=True)
    class Meta:
        model = Contract
        fields = ['id', 'user', 'user_type']

class EventSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_type = UserTypeSerializer(many=False, read_only=True)
    class Meta:
        model = Event
        fields = ['id', 'client', 'user_type']
