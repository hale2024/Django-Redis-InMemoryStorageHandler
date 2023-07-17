from django.contrib import admin
from django.urls import path, include

from .requestHandler import *

urlpatterns = [

    path('handle_post/', handle_post, name='handle_post'),
    
]
