DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db2',
        'USER': 'proksy',
        'PASSWORD': 'proksy',
        'HOST': 'localhost',
        'PORT': '',
    }
}