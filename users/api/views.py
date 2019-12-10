from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from .serializers import UserProfileSerializers
from users.models import UserProfile


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please Provide username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    print(user)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def logoutUser(request):
    print(request.user)
    res = request.user.auth_token.delete()
    return Response({'status': True}, HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signin(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None or username.strip() is '' or password.strip() is '':
        return Response({'error': "Please provide username and password"}, status=HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
        print(user)
        return Response({'error': 'Exist'}, HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        user = User.objects.create_user(username, '', password)

        if not user:
            return Response({'error': 'Invalid Credential'}, HTTP_400_BAD_REQUEST)
        else:
            profile = {
                'user_id': str(user.id),
                'email': str(user)+'@cultivate.com'
            }
            try:
                profileSerializer = UserProfileSerializers(data=profile)
                if profileSerializer.is_valid():
                    profileSerializer.save()
                else:
                    u = user.objects.get(username=user)
                    return Response(profileSerializer.errors, HTTP_400_BAD_REQUEST)
            except:
                return Response(profileSerializer.errors, HTTP_400_BAD_REQUEST)

            return Response(str(user), HTTP_200_OK)
    return Response(0)


@csrf_exempt
@api_view(['GET'])

def userProfile(request):
    profile = UserProfile.objects.get(user_id=request.user.id)
    user = User.objects.get(id=request.user.id)
    serializerProfile = UserProfileSerializers(profile)

    data = {
        'user': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        },
        'profile': serializerProfile.data
    }

    return Response(data, HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def chnagePassword(request):
    newPassword = request.data.get('password')
    print(newPassword)
    if newPassword is None or newPassword is '':
        return Response({'error': 'Invalid Credential'}, status=HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(username=request.user.username)
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'statusText': 'OK'}, HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'No User Found'}, status=HTTP_400_BAD_REQUEST)
