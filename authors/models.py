from django.db import models

# Create your models here.
class Author(models.Model):
    abbreviation = models.CharField(unique=True, max_length=5)
    name = models.CharField(max_length=50, blank=False)
    praenomen = models.CharField(max_length=50, blank=True)
    nomen = models.CharField(max_length=50, blank=True)
    cognomen = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=50, blank=True)

