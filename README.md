## Final Project for Python Course (FullStack)
# Installation 
`git clone https://github.com/awakzdev/Django-Frontend-API ; cd Django-Frontend-API ; pip install -r requirements.txt`



# Changing Database
If at any time you wish to convert back to the original database change the following under `/Ganesha/Settings.py` >


```
MongoDB
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'Django-API',
    }
}


Sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Added an option to import json into project under /MongoDBasJson
