from ..models import Users
from .serializers import UserSerializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
