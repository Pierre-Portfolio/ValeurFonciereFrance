from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/<int:graphId>', views.sendGraph, name='sendGraph'),
    path('index/dynamics/<int:data>/<str:codeDep>', views.sendGraphDynamique, name='sendGraphDynamique'),
]