from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage, name= 'mainpage'),
    path('calc/', views.calc_home, name='calc_home'),
    path('travelo/', views.travelo_home, name='travelo_home'),

] 