from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarSerializer
from core.models import Car
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework import status
from core.models import Car
from cars.serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
import requests
import json
from django.http import HttpResponse
from rest_framework import filters


# Create your views here.


class createCarView(generics.ListCreateAPIView):
    """Create a new car in the system"""
    model = Car
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['make_name', 'model_name']

    def post(self, request):
        global dict_json
        serializer = CarSerializer(data=request.data)
        # r=requests.post(url,serializer)
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/honda?format=json'
        r = requests.get(url)
        url_data = r.json()
        Data_str = json.dumps(url_data)
        if (request.method == 'POST'):
            json_data = json.dumps(request.data)
            dict_json = json.loads(json_data)
            for i in range(0, 504):
                if url_data['Results'][i]['Model_ID'] == int(dict_json['model_id']):
                    serializer=CarSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                    return Response(int(dict_json['model_id']), status=status.HTTP_201_CREATED)
            return Response("Not found Cannot add the data to the database", status=status.HTTP_400_BAD_REQUEST)
            # make_name=request.POST['make_name']
            # model_name=serializer.data.get('Model_name')
            # PARAMS={'Make_name':make_name, 'Model_name':model_name}
            # r=request.post(url=url, json={"make_name":make_name, "model_name": model_name})
            # return Response("Not found", status=status.HTTP_201_CREATED)
