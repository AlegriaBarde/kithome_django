from django.contrib import admin
from django.urls import path, include
from .views import index,home

urlpatterns = [
    path('',home,name="home"),
    path('paginahome/',home,name="home"),
]
