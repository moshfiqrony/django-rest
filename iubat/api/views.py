from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND
)
from django.shortcuts import get_object_or_404
from .serializers import StudentProfileSerializers
from rest_framework.views import APIView
from ..models import StudentProfile


class Students(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        student = {
            'user_id': request.user.id,
            'personal_email': request.data.get('email')
        }
        studentSerializer = StudentProfileSerializers(data=student)
        if studentSerializer.is_valid():
            res = studentSerializer.save()
            print(res)
            return Response(studentSerializer.data, HTTP_200_OK)
        else:
            return Response(studentSerializer.errors, HTTP_403_FORBIDDEN)

    def put(self, request):
        saved_student = get_object_or_404( StudentProfile.objects.all(), user_id=request.user.id)
        data = {
            'firstname': request.data.get('firstname'),
            'lastname': request.data.get('lastname'),
        }
        serializer = StudentProfileSerializers(instance=saved_student, data=data, partial=True)
        if serializer.is_valid():
            saved_student  = serializer.save()
            return Response({"success": "Student '{}' updated successfully".format(saved_student.personal_email)}, HTTP_200_OK)
        else:
            return Response(0, HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def addStudent(request):
    student = {
        'user_id': request.user.id,
        'personal_email': request.data.get('email')
    }
    studentSerializer = StudentProfileSerializers(data=student)
    if studentSerializer.is_valid():
        res = studentSerializer.save()
        print(res)
        return Response(studentSerializer.data, HTTP_200_OK)
    else:
        return Response(studentSerializer.errors, HTTP_403_FORBIDDEN)


@csrf_exempt
@api_view(['PUT'])
def updateStudent(request):
    saved_studetn = get_object_or_404(StudentProfile.objects.all(), user_id=request.user.id)
    student = {
        'firstname': request.data.get('firstname'),
        'lastname': request.data.get('lastname'),
    }
    studentSerializer = StudentProfileSerializers(instance=saved_studetn, data=student, partial=True)
    if studentSerializer.is_valid():
        res = studentSerializer.save()
        return Response({'success': res.personal_email}, HTTP_200_OK)
    else:
        return Response(studentSerializer.errors, HTTP_403_FORBIDDEN)
