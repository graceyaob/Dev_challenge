from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('sign-in/', views.signin),
    path('sign-up/', views.signup),
]
