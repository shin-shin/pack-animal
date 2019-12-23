from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from datetime import date, timedelta
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Destination, Day, Activity, Item
from django.contrib.auth.mixins import LoginRequiredMixin


import os
# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def attractions(request):
    return render(request, "destinations/attractions.html")

def dashboard(request):
    destinations = Destination.objects.filter(user = request.user)
    context = {
      'destinations': destinations
    }
    return render(request, "destinations/dashboard.html", context)


def destination(request, destination_id):
    destination = Destination.objects.get(id=destination_id)

    context = {
      'destination': destination,
      # 'days': Day.days_set.all
    }
    return render(request, "destinations/destination.html", context)

def packing(request):
    return render(request, "destinations/packing.html")

def discover(request):
    return render(request, "destinations/discover.html")

def day(request):
    return render(request, "destinations/day.html")

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class DestinationCreate(CreateView):
  model = Destination
  fields = ['location', 'start_date', 'end_date']
  print (f'model is {model}')

  def add_days(self, destination_id):
    destination = Destination.objects.get(id = destination_id)
    destination.save()
    print (f'destination is {destination}')
    start_date = destination.start_date
    end_date = destination.end_date
    print (f'start_date is {start_date}')
    print (f'end_date is {end_date}')


    delta = end_date - start_date
    for i in range(delta.days + 1):
      day = Day(date=start_date + timedelta(days=i), destination_id=destination_id)
      day.save()
      print (f'day is {day}')
    return day

  def form_valid(self, form):
    # Assign the logged in user
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)


