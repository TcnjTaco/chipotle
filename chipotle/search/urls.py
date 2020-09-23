from django.urls import path

from .views import *

urlpatterns = [
    path('search/', Search.as_view(), name='Search'),
    path('', Homepage.as_view(), name='Home'),
]