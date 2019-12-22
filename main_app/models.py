from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Destination(models.Model):
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'trip to {self.location} from {self.start_date} to {self.end_date}'
    
    class Meta:
        ordering = ['-start_date']

class Day(models.Model):
    date = models.DateField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.date} at {self.destination}'

class Activity(models.Model):
    name = models.CharField(max_length=200)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} on {self.day}'

class Item(models.Model):
    name = models.CharField(max_length=200)
    is_checked = models.BooleanField(default=False)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} for a trip to {self.destination}'

   