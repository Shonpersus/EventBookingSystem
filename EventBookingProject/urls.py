"""
URL configuration for EventBookingProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('index.html', views.home, name='homepage'),
    path('auths/', include('auths.urls')),
    path('speakers.html', views.speakers, name='speakers'),
    path('pages/', include('pages.urls')),
    path('schedule.html/', views.schedule, name='schedule'),
    path('sponsors.html/', views.sponsors, name='sponsors'),
    path('news-single.html/', views.news, name='news'),
    path('auth/register.html/', views.register, name='register'),
    path('auth/login.html/', views.login, name='login'),
    path('auth/logout.html/', views.logout, name='logout'),
    path('contact.html/', views.contact, name='contact'),
]
