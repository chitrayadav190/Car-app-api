from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Car


class CarSerializer(serializers.ModelSerializer):
    """Serializer for the cars object"""
    class Meta:
        model= Car
        fields=['make_id','make_name','model_id','model_name']

    def create(self, validated_data):
        """Create a new car and return it"""
        return Car.objects.create(**validated_data)
#he used () instead of [] in fields