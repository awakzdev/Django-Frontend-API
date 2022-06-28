## Final Project for Python Course (FullStack)

<p align="center">
  <img src="https://github.com/awakzdev/Django-Frontend-API/blob/master/logo.png">
</p>


# Installation 
`git clone https://github.com/awakzdev/Django-Frontend-API ; cd Django-Frontend-API ; pip install -r requirements.txt`


# Configuration

###### This project has to be configured to be able to run properly.

**you can skip this by cloning the sqlite repository**

`git clone --branch sqlite https://github.com/awakzdev/Django-Frontend-API`

###### Please follow one of the options below.

- Add data manually through the /admin panel - you'll have to create a superuser `python3 manage.py createsuperuser`

- Add data to MongoDB from json under /API-JSON

- Revert back to the original database by changing the following under `/Ganesha/Settings.py` >
***

```
MongoDB
----------------
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'Django-API',
    }
}


Sqlite
----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
