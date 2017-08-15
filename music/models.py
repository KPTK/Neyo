import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class Album(models.Model):

    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=600)
    genre = models.CharField(max_length=100)
    call_to_action=models.CharField(max_length=150, default='')
    album_logo = models.FileField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title