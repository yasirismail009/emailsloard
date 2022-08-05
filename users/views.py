import traceback
from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes


from utils.responses import ok, created, bad_request, unauthorized, internal_server_error
from users.models import User
from users.serializers import LoginRequestSerializer, UserSerializer, RegisterRequestSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    try:
        register_serializer = RegisterRequestSerializer(data=request.data)

        if register_serializer.is_valid():
            user_serializer = UserSerializer(data=request.data)
            if not user_serializer.is_valid():
                return bad_request(data=user_serializer.errors, message='Failed to register a new user')

            user = user_serializer.save()
            user_data = user_serializer.data
            del user_data['password']
            token, _created = Token.objects.get_or_create(user=user)
            data = {'user': {'role': 'admin', 'data': user_data}, 'token': 'token ' + token.key}

            return created(data=data, message='New user successfully registered')

        return bad_request(data=register_serializer.errors, message='Failed to register a new user')

    except Exception:
        return internal_server_error(message='Failed to register a new user')


@api_view(['POST', 'GET'])
@permission_classes((AllowAny,))
def login(request):
    try:
        # Login with email and password
        if request.method == 'POST':
            login_serializer = LoginRequestSerializer(data=request.data)

            if login_serializer.is_valid():
                email = login_serializer.validated_data.get('email')
                password = login_serializer.validated_data.get('password')
                user = authenticate(email=email, password=password)

                if user:
                    user.last_login = datetime.now()
                    user.is_logged_in = True
                    user.save()

                    user_data = UserSerializer(user).data
                    del user_data['password']
                    token, _created = Token.objects.get_or_create(user=user)
                    data = {'user': {'role': 'admin', 'data': user_data}, 'token': 'token ' + token.key}

                    return ok(data=data, message='Successfully logged in')

                return unauthorized(message='Invalid credentials')

            return bad_request(data=login_serializer.errors, message='Failed to login')

        # Login with token
        if request.method == 'GET':
            if request.user.is_authenticated:
                user = User.objects.get(email=request.user.email)
                user.last_login = datetime.now()
                user.is_logged_in = True
                user.save()

                user_data = UserSerializer(user).data
                del user_data['password']
                token, _created = Token.objects.get_or_create(user=user)
                data = {'user': {'role': 'admin', 'data': user_data}, 'token': 'token ' + token.key}

                return ok(data=data, message='Successfully logged in')

            return unauthorized(message='Invalid token')

    except Exception:
        return internal_server_error(message='Failed to login')


@api_view(['GET'])
def logout(request):
    try:
        email = request.user.email
        user = User.objects.get(email=email)
        Token.objects.filter(user=user).delete()
        user.is_logged_in = False
        user.save()
        return ok(message='Successfully logged out')

    except Exception:
        return internal_server_error(message='Error logging out')

