from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Review(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    rating=models.DecimalField(max_digits=3 ,decimal_places=1)
    def __str__(self):
        return self.owner.username+'-'+str(self.movie)