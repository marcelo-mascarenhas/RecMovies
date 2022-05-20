#!/bin/bash

pipenv install django
pipenv install djangorestframework django-cors-headers
python manage.py runserver