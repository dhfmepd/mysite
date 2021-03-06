from .base import *

INSTALLED_APPS = [
    'mptt',
    'common.apps.CommonConfig',
    'board.apps.BoardConfig',
    'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

ALLOWED_HOSTS = ['52.90.236.160']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

""" MySQL 접속 방식 """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 사용하려는 DB 이름
        'NAME': 'mysite',
        # 여기부터 connection 정보
        'USER' : 'mysite',
        'PASSWORD' : '1qaz!QAZ',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
    }
}