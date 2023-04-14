from django.db import models

# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200, null=True)
    millisecond = models.PositiveIntegerField()
    bytes = models.PositiveIntegerField()
    unitPrice = models.DecimalField(max_digits=4, decimal_places=2)
    album = models.ForeignKey(models.Album)

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(models.Artist)

class Artist(models.Model):
    name = models.ChaField(max_length=200)

