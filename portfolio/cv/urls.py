from django.contrib import admin
from django.urls import path , include
from cv import views

urlpatterns = [
    path ("", views.index, name="home"),
     path ("home", views.home, name="home")
]