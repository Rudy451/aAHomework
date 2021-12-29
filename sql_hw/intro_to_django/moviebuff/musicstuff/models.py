from django.db import models
from django.db.models import Count

# Create your models here.
class Artist(models.Model):
  name = models.CharField(null=False, max_length=80)

  def __init__(self):
    pass

  def n_plus_one_tracks():
    albums = Album.objects.all()
    tracks_count = {}
    for album in albums:
      tracks_count[album.title] = len(Track.objects.filter(album_id=album))
    return tracks_count

  def better_tracks_query():
    return Track.objects.select_related('album_id').values('album_id__title').annotate(Count('album_id__title'))

class Album(models.Model):
  title = models.CharField(null=False, max_length=80)
  artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Track(models.Model):
  title = models.CharField(null=False, max_length=80)
  album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
