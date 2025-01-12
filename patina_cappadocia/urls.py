"""
URL configuration for patina_cappadocia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.shortcuts import render

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '404.html', status=500)

urlpatterns = [
    # Admin URL'sini devre dışı bırak ve yanlış girişleri yönlendir
    path('admin/', RedirectView.as_view(url='/', permanent=True)),
    path('admin', RedirectView.as_view(url='/', permanent=True)),
    
    # Ana uygulama URL'leri
    path('', include('mainapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 404 ve 500 hata sayfaları için handler'ları ayarla
handler404 = 'patina_cappadocia.urls.handler404'
handler500 = 'patina_cappadocia.urls.handler500'
