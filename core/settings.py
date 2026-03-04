import os
import logging
from pathlib import Path

from django.conf.urls.static import static
from django.template.context_processors import media

from decouple import config  # Библиотека для управления переменными окружения

logger = logging.getLogger(__name__)  # Инициализируем логер

# Определяем базовую директорию проекта
BASE_DIR = Path(__file__).resolve().parent.parent


# Секретный ключ приложения, считываемый из переменных окружения
SECRET_KEY = config('SECRET_KEY')

# Режим отладки: включается/выключается через переменные окружения
DEBUG = config('DEBUG', default=False, cast=bool)

# Разрешенные хосты для развертывания проекта
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Список приложений Django (встроенные)
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# Локальные приложения проекта (созданные пользователем)
LOCAL_APPS = [
    'src.app',
]

# Сторонние приложения, установленные через pip
THIRD_PARTY_APPS = [
    'rest_framework',
]

# Полный список установленных приложений
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Корневая конфигурация URL
ROOT_URLCONF = 'core.urls'

# Настройки шаблонов Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-приложение
WSGI_APPLICATION = 'core.wsgi.application'

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST', default='localhost'),
        'PORT': config('POSTGRES_PORT', default='5432'),
    }
}

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Конфигурация для логирования
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': config('DJANGO_LOG_LEVEL', default='INFO'),
            'propagate': False,
        },
    },
}

# Язык и часовой пояс проекта
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"

# Включение интернационализации и поддержки часовых зон
USE_I18N = True
USE_TZ = True

# ===== Настройки для статических файлов =====
STATIC_URL = 'static/'

# ===== Настройки DRF =====
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


