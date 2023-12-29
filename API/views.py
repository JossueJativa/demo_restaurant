from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import base64
import hashlib
import binascii
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import *
from .serializer import *
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password, check_password


def is_base64_sha256(s):
    try:
        # Try to decode the string
        decoded = base64.b64decode(s)
        # Check if it has the correct length for SHA-256
        return len(decoded) == 32
    except (TypeError, binascii.Error):
        return False

@receiver(pre_save, sender=User)
def encrypt_password(sender, instance, **kwargs):
    # Check if the password has been modified
    if instance.pk is None or instance._password != User.objects.get(pk=instance.pk).password:
        # Check if the password is already encrypted with Base64 and SHA
        if not is_base64_sha256(instance.password) and not instance.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2$')):
            raise ValueError('The password is not encrypted with Base64 and SHA.')

        # No need to re-encrypt since it's already in the expected format

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Check if the password is already encrypted with Base64 and SHA before creating the user
        password = request.data.get('password')
        if not is_base64_sha256(password):
            return Response({'error': 'The password is not encrypted with Base64 and SHA.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # No necesitas decodificar y re-encriptar la contraseña aquí
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])

            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=['POST'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the user by email
        user = get_object_or_404(User, email=email)

        # Verify password format
        if not is_base64_sha256(password):
            return Response({'error': 'Invalid password format'}, status=status.HTTP_400_BAD_REQUEST)

        # Use check_password to compare hashed password with stored password
        if not check_password(password, user.password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # User authenticated successfully
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class BillHeaderViewSet(viewsets.ModelViewSet):
    queryset = BillHeader.objects.all()
    serializer_class = BillHeaderSerializer