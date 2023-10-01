from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

@api_view(['POST'])
def auth_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None

    if user:
        auth_user = authenticate(request, username=username, password=password)
        if auth_user:
            login(request, auth_user)
            return Response({'message': 'Successfully Logged In'})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'User created and logged in successfully.'})
    
    return Response({'message': 'Invalid request data'}, status=status.HTTP_400_BAD_REQUEST)
