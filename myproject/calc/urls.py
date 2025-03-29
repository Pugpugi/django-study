from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name= 'calc_home'),
    path('add', views.add, name = 'add')

] 