from django.urls import path
from firstApp import views

urlpatterns = [
    path('index',views.index,name='index')
]