# django_firebase
using firebase as host for django web app

# Configure Firebase
Log into the firebase console and create a new project, name it whatever you wish.
Navigate to authentication on dashboard and set sign in method Email/Password to enable
For first time add a manual user
Now navigate to project overview and select Add Firebase to WebApp now, copy config's for later use in django.

# Installing required modules
You can if you wish to create and virtualenv for django.
Install Django.
The required module for interacting with firebase is pyrebase, you can install it using pip

> pip install django
> pip install pyrebase

# Working with Django
Now we need a new django project, create django project using

> django-admin startproject firelog .		
(you can name it whatever you want by replacing dot)

> cd firelog
> python manage.py runserver