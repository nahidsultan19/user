from django.db import models

Genre = (
    ('Rock', 'Rock'),
    ('Metal', 'Metal'),
    ('Folk', 'Folk'),
    ('Pop', 'Pop'),
)


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    album_title = models.CharField(max_length=100)

    def __str__(self):
        return self.album_title


class Track(models.Model):
    title = models.CharField(max_length=100)
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.CharField(choices=Genre, max_length=10)
    len = models.FloatField(null=True, blank=True)
    rating = models.IntegerField(null=True)
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
