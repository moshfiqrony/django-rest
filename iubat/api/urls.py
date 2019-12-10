from .views import login, logoutUser, signin, userProfile, chnagePassword
from django.urls import path


urlpatterns = [
    path('login/', login),
    path('logout/', logoutUser),
    path('signin/', signin),
    path('profile/', userProfile),
    path('changePassword/', chnagePassword),
]
