from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView

from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationViews(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        org = Organization.objects.all()
        serializer = OrganizationSerializer(org, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            res = serializer.save()
            return Response(res, HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            obj = Organization.objects.get(pk=pk)
            res = obj.delete()
            return Response(res, status=HTTP_200_OK)
        except Organization.DoesNotExist:
            return Response({'error': 'Invalid Primary Key'}, HTTP_400_BAD_REQUEST)
