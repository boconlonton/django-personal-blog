from django.shortcuts import render, redirect

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.wlist, name='wishlist'),
]

