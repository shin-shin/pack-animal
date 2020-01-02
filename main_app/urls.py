from django.urls import path, include
from . import views
from main_app.views import DestinationCreate


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('discover/', views.get_attractions, name='discover'),
    path('new-destination/', views.DestinationCreate.as_view(), name='new_destination'),
    path('destinations/<int:destination_id>/packing/', views.ItemList.as_view(), name='items'),
    path('destinations/<int:destination_id>/packing/<int:pk>/delete/', views.delete_item, name='item_delete'),

    path('destinations/<int:pk>/update/', views.DestinationUpdate.as_view(), name='destination_update'),
    path('destinations/<int:pk>/delete/', views.DestinationDelete.as_view(), name='destination_delete'),

    path('destinations/<int:destination_id>/day/<int:pk>/', views.DayDetail.as_view(), name='day'),
    path('destinations/<int:destination_id>/day/<int:pk>/delete/', views.delete_activity, name='delete_day_activity'),

    path('destinations/<int:destination_id>/', views.destination, name='destination'),
    path('destinations/', views.dashboard, name='dashboard'),

    path('attractions/<int:destination_id>/', views.attractions, name='attractions'),
    path('attractions/<int:destination_id>/day/<int:pk>/add/', views.attr_to_itin, name='attr_to_itin'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup')
]