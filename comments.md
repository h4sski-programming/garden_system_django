

# Commandline activity


1. Virtual env

`python3 -m venv venv`

`source venv/bin/activate`


2. Install Django

`pip install Django`


3. Create Django project

`django-admin startproject garden_system`


4. Activate django server

Move to project folder `cd garden_system`. The folder where is locatec file `manage.py`.

`python3 manage.py runserver`

`Ctrl + C` to stop server.


5. Create the app

`python manage.py startapp garden_app`


6. Migrations in DataBase

`python manage.py migrate`

`python manage.py makemigrations garden_app`


7. Createsuperuser

`python3 manage.py createsuperuser`

username
: h4sski

mail
: h4ssk.programming+garden_system_django@gmail.com

pass
: h4sski



# Help links

- Django tutorial
    - https://docs.djangoproject.com/en/4.2/intro/tutorial01/
