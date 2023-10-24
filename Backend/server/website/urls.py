from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('listings.html', views.listings, name='listings'),
    path('resources.html', views.resources, name='resources'),
    path('submit.html', views.submit, name='submit'),
]

