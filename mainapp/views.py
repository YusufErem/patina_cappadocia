from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def rooms(request):
    return render(request, 'rooms.html')

