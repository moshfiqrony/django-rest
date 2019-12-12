# django-rest
This is a boiler plate or practice project for django rest framework.
I will practice all possible steps for django rest api. You can clone or fork and practice from it.

# How to download?
To download it you have to clone the project to your local machine
```
git clone https://github.com/moshfiqrony/django-rest.git
```
# How to use?
To use it you need [PyChamr](https://www.jetbrains.com/pycharm/download/#section=linux) , [Visual Studio Code](https://code.visualstudio.com/)
```
cd django-res
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
# How to create super user
```
python manage.py createsuperuser
```
[http://localhost:8000](http://localhost:8000)

# What it have now?

## Models
1. users model
2. iubat model

## Funtions or api endpoints
1. /api/user/signin/ - registration with no permission required.
2. /api/user/login/ - login with no permission required.
3. /api/usre/logout/ - logout user need a Authorization Token in header
4. /api/user/profile/ - to get user profile you must call the api with a Authorization Token in header
5. /api/user/changePassword/ - to reset an user password you must call the api with a Authorization Token in header.
6. /api/iubat/addstudent/ - to add a student an user at first need to signin then call the api with a valid email address
7. /api/iubat/updatestudent/ - to update student profile info
8. /api/iubat/student/ - accepts POST GET PUT method for student profile
