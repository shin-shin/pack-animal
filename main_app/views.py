from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
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
    return render(request, "attractions.html")

def dashboard(request):
    return render(request, "menu/dashboard.html")

def new_destination(request):
    return render(request, "menu/new_destination.html")

def destination(request):
    return render(request, "menu/destination.html")

def packing(request):
    return render(request, "menu/packing.html")

def discover(request):
    return render(request, "menu/discover.html")

def day(request):
    return render(request, "menu/day.html")

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

class DestinationCreate(LoginRequiredMixin, CreateView):
  model = Destination
  fields = ['location', 'start_date', 'end_date']