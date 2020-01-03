from django.db import models
from django.urls import reverse
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.dispatch import receiver #import @receiver decorator, to connect signal with function
from django.db.models.signals import post_save #module defines a set of signals sent by the model system

import calendar
# Create your models here.

class Destination(models.Model):
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.location}({self.id}) from {self.start_date} to {self.end_date}'
    
    def get_absolute_url(self):
        return reverse('destination', kwargs={'destination_id': self.id})

    def item_for_destination(self):
        return self.item_set.filter(destination_id=self.id)

    class Meta:
        ordering = ['-start_date']

class Day(models.Model):
    date = models.DateField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('day_detail', kwargs={'day_id': self.id})

    def __str__(self):
        return f'{self.date} at {self.destination} with id {self.id}'

    class Meta:
        ordering = ['date']

class Activity(models.Model):
    name = models.CharField(max_length=200)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} on {self.day}'


class Item(models.Model):
    name = models.CharField(max_length=200)
    is_checked = models.BooleanField(default=False)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse('item_list', kwargs={'destination_id': destination.id})

    def __str__(self):
        return f'{self.name}'

@receiver(post_save, sender=Destination) # post_save signal is sent at the end of the save() method
def post_save_destination(sender,instance,created, **kwargs):
    print (f'post_save_destination is called')
    if created:
        current_date = instance.start_date
        while current_date <= instance.end_date:
            day = Day(date=current_date, destination_id=instance.id)
            day.save()
            current_date = current_date + timedelta(days=1)
    else:
        new_dates = []
        excisting_dates = []

        current_date = instance.start_date
        while current_date <= instance.end_date:
            new_dates.append(current_date)
            current_date = current_date + timedelta(days=1)

        day_records = Day.objects.filter(destination_id=instance.id)
        for record in day_records:
            excisting_dates.append(record.date)

        for d in new_dates:
            print (f'new date is {d}')    
            if d not in excisting_dates:
                print (f'new date is new')    
                day = Day(date=d, destination_id=instance.id)
                day.save()     
            else:
                print (f'new date already exists, skipping')     

        for d in excisting_dates:
            if d not in new_dates:
                Day.objects.filter(destination_id=instance.id, date=d).delete()
            else:
                print (f'exiting date still exists')    