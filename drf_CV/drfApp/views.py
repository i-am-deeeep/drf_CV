from django.shortcuts import render
from .models import Movie,Review
from .serializers import MovieSerializer,ReviewSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsReviewUserOrReadOnly


# Create your views here.

class MovieListCV(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class MovieDetailCV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer


class ReviewListCV(generics.ListCreateAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(movie=pk)
    def perform_create(self,serializer):
        movie=self.kwargs['pk']
        movie=Movie.objects.get(pk=movie)
        serializer.save(movie=movie,owner=self.request.user)

class ReviewDetailCV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsReviewUserOrReadOnly]