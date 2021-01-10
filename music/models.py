from django.db import models

Genre = (
    ('Rock', 'rock'),
    ('Metal', 'metal'),
    ('Folk', 'folk'),
    ('Pop', 'pop'),
)


class Artist(models.Model):
    name = models.CharField(max_length=100)


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(choices=Genre, max_length=10)


class Track(models.Model):
    title = models.CharField(max_length=100)
    len = models.IntegerField()
    rating = models.IntegerField()
    count = models.IntegerField()
