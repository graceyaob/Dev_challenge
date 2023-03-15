from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('sign-in/', views.signin, name="signin"),
    path('sign-up/', views.signup, name="signup"),
]
