from django.contrib import admin
from .models import Destination, Day, Activity, Item

# Register your models here.
admin.site.register(Destination)
admin.site.register(Day)
admin.site.register(Activity)
admin.site.register(Item)
