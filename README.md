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

1. Now we need to makemigrations and migrate
2. Create a templates folder for our sign_in and welcome pages
3. Set the templates folder path in settings.py
4. Create views.py file for our sign_in and welcome views
5. Use the pyrebase module for authenticating users with email and password
6. add the urls for our views