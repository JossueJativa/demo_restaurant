from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    # Add a description for the 'password' field
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        required=True,
        help_text="The password should be encrypted using Base64 and SHA-256 for security reasons."
    )

    class Meta:
        model = User
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class BillHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillHeader
        fields = '__all__'