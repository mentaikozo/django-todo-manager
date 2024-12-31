# django-todo-manager

## setup

1. `python -m venv venv`
1. `.\venv\Scripts\activate`
1. `pip install --upgrade pip`
1. `pip install Django`
1. `django-admin startproject TodoManager .`
1. アプリ作成 `python manage.py startapp app`

settings.pyの修正  
- INSTALLED_APP
- LANGUAGE_CODE
- TIME_ZONE
- ALLOWED_HOSTS = ["*"]

## memo

起動  
`python manage.py runserver`

DBの反映  
デフォルトで利用するアプリ(settings.py)もDBを使うので初回も実行する  
`python manage.py migrate`

superuser作成  
`python manage.py createsuperuser`

