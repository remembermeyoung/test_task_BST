from django.contrib import admin
from django.urls import path, include
from .views import download_file

urlpatterns = [
    path('download/', download_file),
]
