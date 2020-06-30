"""playpubg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .import views

urlpatterns = [
    path('', include('loginreg.urls')),
    path('', include('matches.urls')),
    path('', include('user_profile.urls')),
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('live/', views.live, name="live"),
    path('topplayers/', views.top_players, name="top-players"),
    path('rules/', views.rules, name="rules"),
    path('about/', views.about, name="about"),
    
]
