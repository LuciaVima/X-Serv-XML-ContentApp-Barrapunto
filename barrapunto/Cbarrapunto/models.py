from django.db import models

# Create your models here.

class Pages(models.Model):
    name = models.TextField()
    page = models.TextField()

class Barras(models.Model):
    title = models.TextField()
    url = models.TextField()
	
