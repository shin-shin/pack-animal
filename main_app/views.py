from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse
from datetime import date, timedelta
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Destination, Day, Activity, Item
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ItemForm, ActivityForm


import os
import calendar
# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def attractions(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    context = {
        'destination': destination
    }
    return render(request, "destinations/attractions.html", context)


def dashboard(request):
    destinations = Destination.objects.filter(user=request.user)
    context = {
        'destinations': destinations
    }
    return render(request, "destinations/dashboard.html", context)


def destination(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    days = destination.day_set.all()

    for d in days:
        d.weekday = calendar.day_name[d.date.weekday()]

    context = {
        'destination': destination,
        'days': days
    }
    return render(request, "destinations/destination.html", context)


class ItemList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        self.form = ItemForm(self.request.GET or None,)
        return super(ItemList, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = ItemForm(self.request.POST or None)
        if self.form.is_valid():
            new_item = self.form.save(commit=False)
            new_item.destination_id = self.kwargs['destination_id']
            new_item.save()
        else:
            return super(ItemList, self).post(request, *args, **kwargs)
        return redirect('items', destination_id=self.kwargs['destination_id'])

    def get_queryset(self):
        print("Destination id ", self.kwargs['destination_id'])
        return Item.objects.filter(destination_id=self.kwargs['destination_id'])

    def get_context_data(self, **kwargs):
        context = super(ItemList, self).get_context_data(**kwargs)
        # context['item_form'] = ItemForm()
        context['destination'] = Destination.objects.get(
            id=self.kwargs['destination_id'])
        return context


# def add_item(request, destination_id):
#     # create the ModelForm using the data in request.POST
#     form = ItemForm(request.POST)
#     # validate the form
#     if form.is_valid():
#         new_item = form.save(commit=False)
#         new_item.destination_id = destination_id
#         new_item.save()
#     return redirect('items', destination_id=destination_id)


def discover(request):
    location = request.POST.get('location', '')
    print(f'location is {location}')
    return render(request, "discover.html", {'location': location})


class DayDetail(LoginRequiredMixin, DetailView):
    model = Day

    def get(self, request, *args, **kwargs):
        self.form = ActivityForm(self.request.GET or None,)
        # destination_id=self.kwargs['destination_id']
        # day_id=self.kwargs['pk']
        return super(DayDetail, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = ActivityForm(self.request.POST or None)
        if self.form.is_valid():
            new_activity = self.form.save(commit=False)
            new_activity.day_id = self.kwargs['pk']
            new_activity.save()
        else:
            return super(DayDetail, self).post(request, *args, **kwargs)
        return redirect('day', destination_id=self.kwargs['destination_id'], pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(DayDetail, self).get_context_data(**kwargs)
        context['weekday'] = calendar.day_name[self.object.date.weekday()]
        context['activities'] = Activity.objects.filter(day_id=self.kwargs['pk'])
        return context


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


class DestinationCreate(CreateView):  # works
    model = Destination
    fields = ['location', 'start_date', 'end_date']

    def form_valid(self, form):
        # Assign the logged in user
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class DestinationUpdate(UpdateView):  
    model = Destination
    fields = ['location', 'start_date', 'end_date']

    def form_valid(self, form):
        # Assign the logged in user
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class DestinationDelete(DeleteView):  # works
    model = Destination
    success_url = '/destinations/'
