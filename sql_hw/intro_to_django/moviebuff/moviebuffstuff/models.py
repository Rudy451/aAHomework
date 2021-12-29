from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Movies(models.Model):
  title = models.CharField(max_length=80, db_index=True, null=False)
  yr = models.IntegerField(RegexValidator(r'^[0-9]{4}$', 'Fomrat: XXXX'), db_index=True, null=False)
  score = models.FloatField(null=False)
  votes = models.IntegerField(null=False)
  director_id = models.IntegerField(db_index=True, null=False)

class Actors(models.Model):
  name = models.CharField(max_length=80, null=False)

class Castings(models.Model):
  ord = models.IntegerField(null=False)
  actor_id = models.ForeignKey(Actors, db_index=True, null=False, on_delete=models.CASCADE)
  movie_id = models.ForeignKey(Movies, db_index=True, null=False, on_delete=models.CASCADE)
