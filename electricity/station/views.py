from django.shortcuts import render
from .models import Station
from .serializer import StationSerializer
from rest_framework import generics

class StationAPIView(generics.ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

