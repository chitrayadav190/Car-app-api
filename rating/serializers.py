from rest_framework import serializers
from core.models import Rating

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Rating
        fields=['car', 'car_rating']
