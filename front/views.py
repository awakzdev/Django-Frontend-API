from django.shortcuts import render
import requests


def home(request):
    response = requests.get('http://127.0.0.1:8000/api/workers/')
    worker = response.json()

    return render(request, "home.html", {'users': worker})