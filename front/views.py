from django.shortcuts import render
import requests


def home(request):
    response = requests.get('http://127.0.0.1:8000/api/workers/')
    r_response = requests.get('http://127.0.0.1:8000/api/speciality/')

    users = response.json()
    speciality = r_response.json()

    return render(request, "home.html", context={'users': users, 'speciality': speciality})
