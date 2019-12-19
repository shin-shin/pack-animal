from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Destination(models.Model):
    location = models.CharField(max_length=100)
    dates=models.DateField()
    completed=models.IntegerField("completed", default=0)