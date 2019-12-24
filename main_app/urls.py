from django.urls import path, include
from . import views
from main_app.views import DestinationCreate


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('discover/', views.discover, name='discover'),
    path('destinations/<int:destination_id>/packing/', views.PackingList.as_view(), name='packing'),
    path('attractions/<int:destination_id>/', views.attractions, name='attractions'),
    
    path('destinations/', views.dashboard, name='dashboard'),
    path('destinations/<int:destination_id>/', views.destination, name='destination'),
    path('destinations/<int:destination_id>/day/<int:pk>/', views.DayDetail.as_view(), name='day'),
    
    path('new-destination/', views.DestinationCreate.as_view(), name='new_destination'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup')
]