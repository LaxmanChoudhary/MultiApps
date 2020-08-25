import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': 'multiapp',
        'USER': 'django',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',

        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
    }


}

DEBUG = True