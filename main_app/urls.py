from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('discover/', views.discover, name='discover'),
    path('packing/<int:d_id>/', views.packing, name='packing'),
    path('attractions/<int:d_id>/', views.attractions, name='attractions'),
    path('destinations/', views.dashboard, name='dashboard'),
    path('destinations/<int:d_id>/', views.destination, name='destination'),
    path('day/<int:day_id>/', views.day, name='day'),
    path('new-destination/', views.new_destination, name='new_destination'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup')
]