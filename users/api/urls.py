from django.conf.urls import url, include
from rest_framework import routers
from .views import login, logoutUser
from django.urls import path


urlpatterns = [
    path('login/', login),
    # path('get_data/', getData),
    path('logout/', logoutUser),
]
