from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarSerializer
from core.models import Car
# Create your views here.


class createCarView(generics.ListCreateAPIView):
    """Create a new car in the system"""
    model= Car
    serializer_class=CarSerializer
    queryset = Car.objects.all()
