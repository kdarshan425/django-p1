from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Darshan Admin"
admin.site.site_title = "Darshan Admin Portal"
admin.site.index_title = "Welcome to Darshan Researcher Portal"

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]