
# Django App

### Development
**Note** : Make sure you have Python version 4.0

### Environment Setup

`$ git clone https://github.com/Akash1362000/django_project_blogapp.git`

`$ cd news/`

If virtualenv is not installed [(What is virtualenv?)](https://www.youtube.com/watch?v=N5vscPTWKOk&t=313s):

`$ pip install virtualenv`

Create a virtual environment

`$ virtualenv venv`

Activate the environment everytime you open the project

`$ source venv/Scripts/activate`

Install requirements

`$ pip install -r requirements.txt`

Run migrations for Database 

`$ python manage.py makemigrations`

`$ python manage.py migrate`

Create superuser for Admin Login

`$ python manage.py createsuperuser`

Enter your desired username, email and password. Make sure you remember them as you'll need them in future.

eg.

    Username: admin
    
    Email: admin@example.com
    
    Password: <your password>

Configuration

[(SMTP config see)](https://docs.djangoproject.com/en/3.2/topics/email/#smtp-backend)

`$ cp .env.example .env `

All Set!

Now you can run the server to see your application up & running

`$ python manage.py runserver`

To exit the environment

`$ deactivate`

Every time you want to open the application in browser, make sure you run:

`$ source venv/Scripts/activate`

`$ python manage.py runserver`