from django.db import models


class Movie(models.Model):
    imdb_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    poster = models.URLField()
