from django.urls import path, include
from . import views

urlpatterns = [
   path('about-us.html/', views.about_us, name='about_us'),
   path('single-speaker.html/', views.single_speaker, name='single-speaker'),
   path('gallery.html/', views.gallery, name='gallery'),
   path('testimonial.html/', views.testimonial, name='testimonial'),
   path('pricing.html/', views.pricing, name='pricing'),
]
