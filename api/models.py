from django.db import models

class Movie(models.Model):
    title = models.TextField()
    year = models.IntegerField()
    imdbID = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    img_url = models.TextField()