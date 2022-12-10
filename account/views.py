from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import AccountSerializer, AccountFrontendSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def endpoints(request, format=None):
    context = [
        'POST: /register/',
        'GET: /user-credential',
        'POST: /login/',
        'GET: /logout',
    ]

    return Response(context)


@api_view(['POST'])
def register(request, format=None):
    """Register a user. This function intended only for client registration

    Method: POST

    Args:
        request (dictionary): data contains client's {email, username and password}

    Returns:
        none: none
    """
    serializer = AccountFrontendSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def frontend_detail(request, format=None):
    """Getting user access token saved browser cookie works on api only

    Method: GET

    Returns:
        string: Access token

    Route:
        account/user-credential/
    """
    jwt = JWTAuthentication()
    token = request.COOKIES.get('access')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        validated = jwt.get_validated_token(token)
    except:
        AuthenticationFailed('Unauthenticated')

    username = jwt.get_user(validated)
    user = User.objects.filter(username=username).first()
    serializer = AccountFrontendSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def login_view(request, format=None):
    """Login registered user then save access token to cookies

    Raises:
        AuthenticationFailed: If username not found or incorrect
        AuthenticationFailed: If password not found or incorrect

    Method: POST

    Returns:
       string : Access token

    Route:
        account/login/<str:email,str:password>
    """
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()
    if user is None:
        raise AuthenticationFailed("User not found!")

    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password!')

    refresh = RefreshToken.for_user(user)
    access = str(refresh.access_token)
    response = Response()

    response.set_cookie(key="access", value=access, httponly=True)

    response.data = {
        'access': access
    }
    return response


@api_view(['POST'])
def logout_view(request, format=None):
    """Logging out user

    Method: POST
    """
    response = Response()
    response.delete_cookie('access')
    response.data = {
        'message': 'User logout successfully'
    }
    return response


@api_view(['GET'])
def get_email(request, username, format=None):
    """Get email using username

    Args:
        username (string): user username

    Returns:
        User email address
    """

    email = User.objects.filter(username=username).first()
    if email is None:
        raise AuthenticationFailed("Username not found!")
    serializer = AccountFrontendSerializer(email, many=False)
    return Response(serializer.data)
