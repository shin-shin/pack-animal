from django.urls import path, include
from . import views
from main_app.views import DestinationCreate


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('discover/', views.discover, name='discover'),
    path('packing/<int:d_id>/', views.packing, name='packing'),
    path('attractions/<int:d_id>/', views.attractions, name='attractions'),
    
    path('destinations/', views.dashboard, name='dashboard'),
    path('destinations/<int:destination_id>/', views.destination, name='destination'),
    path('destinations/<int:destination_id>/day<int:day_id>/', views.day, name='day'),
    
    path('new-destination/', views.DestinationCreate.as_view(), name='new_destination'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup')
]