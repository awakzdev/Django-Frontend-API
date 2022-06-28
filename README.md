## Final Project for Python Course (FullStack)

<p align="center">
  <img src="https://github.com/awakzdev/Django-Frontend-API/blob/master/logo.png">
</p>


# Installation 
`git clone https://github.com/awakzdev/Django-Frontend-API ; cd Django-Frontend-API ; pip install -r requirements.txt`


# Configuration

This project has to be configured to be able to run correctly, to do this please follow either of the instructions below. **alternatively you can skip this by cloning the sqlite repository**

- Add data manually through the /admin panel - you'll have to create a superuser `python3 manage.py createsuperuser`

- Add data to MongoDB from json under /MongoDBasJSON

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
