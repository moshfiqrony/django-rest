from django.urls import path

from .views import OrganizationViews

urlpatterns = [
    path('organization/', OrganizationViews.as_view()),
    path('organization/<int:pk>/', OrganizationViews.as_view()),
]
