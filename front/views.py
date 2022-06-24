from pathlib import Path

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import requests


def home(request):
    response = requests.get('http://127.0.0.1:8000/api/workers/')
    r_response = requests.get('http://127.0.0.1:8000/api/speciality/')

    users = response.json()
    speciality = r_response.json()

    return render(request, "home.html", context={'users': users, 'speciality': speciality})


def review(request):
    from datetime import date
    import requests
    import json
    import os

    # Grab API from Django APP
    url = 'http://127.0.0.1:8000/api/workers/'
    data = requests.get(url)

    # Convert text into json format
    workers = json.loads(data.text)
    data_json = json.dumps(workers, indent=2)
    print(f"List of workers : \n{data_json}")

    # Get average worker salary
    total_salary = 0
    counter = 0
    average_salary = 0
    for person in workers:
        counter += 1
        total_salary += person["salary"]
        average_salary = total_salary / counter
    print(f"Average worker salary is : {average_salary}")

    # Create dates
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    print(f"Current date is - {today}")

    worker_detail = []
    for person in workers:
        worker_year = person['hire_date'][0:4]
        worker_month = person['hire_date'][5:7]
        if year > worker_year and int(month) - 12 + int(worker_month) > 0:
            worker_detail += [person['id']]

    # Grab workers details - if he works more than a year
    reported_workers = []
    for person in workers:
        if person['id'] in worker_detail:
            reported_workers.append(person)
    information = reported_workers

    # prettify and save as a json
    save = json.dumps(information, indent=2)
    print(f"filtered workers : \n{save}")

    # create a dir for text file
    my_file = Path("Saved")
    if my_file.is_dir():
        pass
    else:
        os.mkdir("Saved")

    # empty strings are "falsy" - if true write
    if save:
        with open('Saved/reports.txt', 'w+') as f:
            print('Saving to a text file.')
            f.writelines(f"This will contain all the workers whose salary is below average"
                         f" and are working for over a year\nAverage worker salary is : {average_salary}"
                         f"\nCurrent date - {today}\n{save}")

    messages.success(request, 'Please check your console or alternatively the /Saved folder.')
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
