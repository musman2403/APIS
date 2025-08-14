# accounts/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.authtoken.models import Token

# Register user
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", "")
    phone = request.data.get("phone", "")

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    profile = UserProfile.objects.create(user=user, phone=phone)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        "user": UserSerializer(user).data,
        "profile": UserProfileSerializer(profile).data,
        "token": token.key
    }, status=status.HTTP_201_CREATED)


# Login user
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)

    if user is None:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        "token": token.key,
        "user": UserSerializer(user).data
    })


# Logout user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({"message": "Logged out successfully"})


# Profile view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    return Response(UserProfileSerializer(profile).data)
