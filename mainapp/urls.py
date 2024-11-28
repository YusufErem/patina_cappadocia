from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<slug:room_name>/', views.room_details, name='room_details'),
    path('booking/', views.booking, name='booking'),

]