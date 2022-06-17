from datetime import date
import requests
import json
import logging
import sys

# Create Logger
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler(filename="info.log"),
                        logging.StreamHandler(sys.stdout)
                    ])
logger = logging.getLogger()


def project():
    # Grab API from Django APP
    url = 'http://127.0.0.1:8000/workers/'
    data = requests.get(url)

    # Convert text into json format
    workers = json.loads(data.text)
    data_json = json.dumps(workers, indent=2)
    logger.info(f"List of workers : \n{data_json}")

    # Get average worker salary
    total_salary = 0
    counter = 0
    average_salary = 0
    for person in workers:
        counter += 1
        total_salary += person["salary"]
        average_salary = total_salary / counter
    logger.info(f"Average worker salary is : {average_salary}")

    # Match current date with workers 'hire_date'
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    logger.info(f"Current date is - {today}")

    worker_detail = []
    for person in workers:
        worker_year = person['hire_date'][0:4]
        worker_month = person['hire_date'][5:7]
        if year > worker_year and int(month) - 12 + int(worker_month) > -1:
            worker_detail += [person['id']]

    # Grab workers details - if he works more than a year
    information = {}
    reported_workers = []
    for person in workers:
        if person['id'] in worker_detail:
            reported_workers.append(person)
    information = reported_workers

    # prettify and save as a json
    save = json.dumps(information, indent=2)
    logger.info(f"filtered workers : \n{save}")

    # empty strings are "falsy" - if true write
    if save:
        with open('reports.txt', 'w+') as f:
            logger.info('Saving to a text file.')
            f.writelines(save)


if __name__ == "__main__":
    project()
