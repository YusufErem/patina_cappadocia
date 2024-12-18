from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms, name='rooms'),

    path('book/', views.book, name='book'),
    path('book/checkout/', views.book, name='checkout'),


]