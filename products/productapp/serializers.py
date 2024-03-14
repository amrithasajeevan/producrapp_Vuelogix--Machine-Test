from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ['id', 'username', 'email', 'phone', 'password']

    

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    password=serializers.CharField(max_length=15)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'size', 'color', 'status']



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'username', 'product', 'quantity', 'date_ordered']