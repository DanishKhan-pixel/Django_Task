# django_app/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import random

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create_random_user(self, request):
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
        name = random.choice(names)
        email = f'{name.lower()}@example.com'
        password = 'password123'  # Use a secure password in production

        user = User.objects.create_user(email=email, name=name, password=password)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
