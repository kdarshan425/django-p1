from django.db import models


# Create your models here.

class Conection_eg(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.TextField(max_length=255)
    
    