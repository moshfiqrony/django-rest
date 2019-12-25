from django.urls import path
from django.conf.urls import url

from .views import MyChannelViews

urlpatterns = [
    url(r'^$', MyChannelViews.as_view()),
]
