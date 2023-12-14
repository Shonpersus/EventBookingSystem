from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='registration-url'),
    path('login/', views.login, name='login-url'),
    path('logout/', views.logout, name='logout-url')
]