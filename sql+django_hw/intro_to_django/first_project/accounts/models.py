from django.db import models

# Create your models here.
class MyUser(models.Model):

  user_name = models.CharField(max_length=80)
  password = models.CharField(max_length=80)
  session_token = models.BooleanField
