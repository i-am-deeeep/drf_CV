from .models import Movie,Review
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta():
        model=Movie
        fields="__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model=Review
        fields="__all__"
        read_only_fields=['movie','owner']
    movie=serializers.StringRelatedField()
    owner=serializers.StringRelatedField()