from django.db import models
from django.urls import reverse
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

import calendar
# Create your models here.

class Destination(models.Model):
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'trip to {self.location}({self.id}) from {self.start_date} to {self.end_date}'
    
    def get_absolute_url(self):
        return reverse('destination', kwargs={'destination_id': self.id})

    class Meta:
        ordering = ['-start_date']

class Day(models.Model):
    date = models.DateField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('day_detail', kwargs={'day_id': self.id})

    def __str__(self):
        return f'{self.date} at {self.destination} with id {self.id}'

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


@receiver(post_save, sender=Destination)
def post_save_destination(sender,instance,created, **kwargs):
    print (f'post_save_destination is called')
    if created:
        print (f'destination is {instance. location}')
        current_date = instance.start_date
        while current_date <= instance.end_date:
            print (f'current_date is {current_date}')    
            day = Day(date=current_date, destination_id=instance.id)
            day.save()
            current_date = current_date + timedelta(days=1)
