from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.restro_signup , name='restro_signup'),
    path('login/', views.restro_login , name='restro_login'),
    # path('', views.restro_signup , name='restro_signup'),
]
