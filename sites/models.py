from django.db import models

# Create your models here.
class MusicList(models.Model):

    numbering = models.IntegerField()
    published_date = models.DateField()
    type = models.CharField(max_length=32)
    cd_title = models.CharField(max_length=200)
    disk = models.IntegerField()
    track = models.IntegerField()
    music_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    arranger = models.CharField(max_length=100)

    def __str__(self):
        return self.music_title