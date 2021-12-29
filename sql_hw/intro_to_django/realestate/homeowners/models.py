from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Person:
  pass

class House(models.Model):
  # home address
  address = models.CharField(max_length=30, validators=[RegexValidator('^[0-9]{3,} [A-Za-z]{3,} [Az-az{3,}]$', "Use format: street number + street name")]);

class Person(models.Model):
  # name
  name = models.CharField(max_length=15)
  # house id
  house_id = models.OneToOneField(House, null=True, on_delete=models.CASCADE)
