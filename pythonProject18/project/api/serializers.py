from rest_framework import serializers
from .models import Products, Cart, Order, User

class LoginSer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class Regserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'fio', 'password']

    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            fio = self.validated_data['fio'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CartSer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class OrderSer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
