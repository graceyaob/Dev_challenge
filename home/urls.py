from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('sign-in/', views.signin, name="signin"),
    path('sign-up/', views.signup, name="signup"),
    path('statistics/', views.statistics, name="stats"),
    path('forgot-password', views.forgot_password, name="password.recovery"),
    path('stations-list', views.stations, name="stations"),
    path('station/<str:station_name>/check', views.station_check, name="stations.check"),
]
