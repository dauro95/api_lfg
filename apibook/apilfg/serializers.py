from dataclasses import fields
from rest_framework import serializers
from .models import *

class VideogameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogame
        fields = '__all__'

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class Party_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Party_user
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'