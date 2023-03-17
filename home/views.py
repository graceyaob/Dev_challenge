from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
import requests
from django.contrib import messages

# Create your views here.

def index(request):
    # return HttpResponse('hello world !')
    return render(request, 'home/index.html', {})

def signin(request):
    return render(request, 'home/sign-in.html', {})

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        print("post")

    print("after if post")

    context = {
        'form': form,
    }
    return render(request, 'home/sign-up.html', context)

def statistics(request):
    context = {}
    return render(request, 'home/statistics.html', context)

def forgot_password(request):
    context = {}
    return render(request, 'home/sign-in.html', context)

def stations(request):
    url = "https://airqino-api.magentalab.it/getStations/Arezzo"
    context = {
        'stations': requests.get(url).json()
    }
    print(stations)
    return render(request, 'home/stations.html', context)

def station_check(request, station_name):
    url = "https://airqino-api.magentalab.it/getCurrentValues/" + station_name
    context = {
        'station': requests.get(url).json()
    }
    print(context['station'])
    return render(request, 'home/sensors.html', context)
    