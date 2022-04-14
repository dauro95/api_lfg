from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class VideogameViewSet(viewsets.ModelViewSet):
    queryset = Videogame.objects.all().order_by('name')
    serializer_class = VideogameSerializer

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all().order_by('name')
    serializer_class = PartySerializer

class PartyuserViewSet(viewsets.ModelViewSet):
    queryset = Party_user.objects.all().order_by('start_date')
    serializer_class = Party_userSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('created_date')
    serializer_class = MessageSerializer
