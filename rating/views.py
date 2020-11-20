from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework import status
from core.models import Rating

from rest_framework import serializers
from rating.serializers import RatingSerializer
from django_filters.rest_framework import DjangoFilterBackend
import requests
import json

# Create your views here.
class AddRate(generics.ListCreateAPIView):
    model = Rating
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    filter_backends = [DjangoFilterBackend]

    def post(self, request):
        global dict_json
        serializer = RatingSerializer(data=request.data)
        # r=requests.post(url,serializer)
        if (request.method == 'POST'):
            # json_data = json.dumps(request.data)
            # dict_json = json.loads(json_data)
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(request.data, status=status.HTTP_201_CREATED)
            return Response("Not found Cannot add the data to the database", status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    # def get_queryset(self):
    #     """Return objects"""
    #     return self.queryset.order_by('-rating')