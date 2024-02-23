from django.db import models

# Create your models here.

class movie(models.Model):
    mname=models.CharField(max_length=20)
    mdirector=models.CharField(max_length=20)
    mposter=models.ImageField(upload_to='gallery')
