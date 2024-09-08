from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('udus_lost_and_found.urls')),
    ]