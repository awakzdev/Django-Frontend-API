## Final Project for Python Course (FullStack)

<p align="center">
  <img src="https://github.com/awakzdev/Django-Frontend-API/blob/master/image/logo.png">
</p>

# Configuration

###### This project's database needs to be fed in order to view its properties.

**you can skip this by cloning the sqlite repository**

`git clone --branch sqlite https://github.com/awakzdev/Django-Frontend-API`

<hr></hr>

###### Please follow one of the steps below.

- Add data manually through the /admin panel - you'll have to create a superuser `python3 manage.py createsuperuser`

- Add data to MongoDB from json under /API-JSON

- Revert back to the original database by changing the following under `/Ganesha/Settings.py` >



## MongoDB

```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'Django-API',
    }
}
```

## SQLite
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
