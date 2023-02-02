sudo docker-compose up

Vous devez efectuer la comfig de la base de donner dans setting.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yourdbname', 
        'USER': 'yourdbuser', 
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}



ETAPE 1 : CD P12/Epic_event

ETAPE 2 : python -m pip install --user env

ETAPE 3 : /env/bin/activate

ETAPE 4 : pip install -r requirements.txt

ETAPE 5 : python3 manage.py migrate

ETAPE 6 : python3 manage.py createsuperuser

ETAPE 7 : python3 manage.py runserver



