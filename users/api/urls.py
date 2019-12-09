from django.conf.urls import url, include
from rest_framework import routers
from .views import UserView

router = routers.DefaultRouter()

router.register(r'/users', UserView, base_name='Users')


urlpatterns = router.urls
