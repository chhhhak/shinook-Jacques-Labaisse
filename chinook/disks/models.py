from django.db import models

class Track(models.Model):
    id = models.CharField(max_lenght=200)
    name = models.CharField(max_lenght=200)
    composer = models.CharField(max_lenght=200)
    milliseconds = models.PositiveIntegerField(default=0)
    bytes = models.PositiveIntegerField(default=0)
    unitPrice = models.DecimalField(decimal_places=2, max_digits=4)
    album = models.ForeignKey(models.Album)

class Album(models.Model):
    id = models.CharField(max_lenght=200)
    title = models.CharField(max_lenght=200)
    artist = models.ForeignKey(models.Artist)

class Artist(models.Model):
    id = models.CharField(max_lenght=200)
    name = models.CharField(max_lenght=200)


