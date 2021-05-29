from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/<int:graphId>', views.sendGraph, name='sendGraph'),
]