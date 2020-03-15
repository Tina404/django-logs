"""Defines URL patterns for djlogs."""

from django.urls import path

from . import views

app_name = 'djlogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]