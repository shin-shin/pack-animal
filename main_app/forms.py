from django.forms import ModelForm
from django.forms import modelform_factory
from .models import Destination, Day, Activity, Item

ItemForm = modelform_factory(Item, fields=('name',))
ActivityForm = modelform_factory(Activity, fields=('name',))