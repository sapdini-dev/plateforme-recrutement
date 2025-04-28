from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-r9qvh7o8r36iab813lo4u8xe)j*nfvm5s1+x%g*=g1psor&!+b'

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',  # Pour le local
    'localhost',  # Pour le local
    'plateforme-recrutement.onrender.com',  # Ajouter le domaine Render
    'www.plateforme-recrutement.onrender.com',  # Si tu veux également inclure le domaine avec "www"
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'plateforme',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestion_recrutement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestion_recrutement.wsgi.application'

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'ins'),  # Nom de la base de données
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),  # Hôte de la base
        'USER': os.environ.get('DB_USER', 'root'),  # Utilisateur
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),  # Mot de passe
        'PORT': os.environ.get('DB_PORT', '3306'),  # Port de la base
    }
}


LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'Europe/Paris'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Dossier où les fichiers statiques seront collectés


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
