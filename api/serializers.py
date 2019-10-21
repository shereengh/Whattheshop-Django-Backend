from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Meal, MealOrder, Profile, Order
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        # ...

        return token


class MealOrderSerializer(serializers.ModelSerializer):
    meal = MealSerializer()
    class Meta:
        model = MealOrder
        fields = ["meal","quantity"]

class ProfileSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    orders_list = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["user","profilepic", "firstname", "lastname","contact", "email", "orders_list"]

    def get_orders_list(self, obj):
        mealorders = Order.objects.filter(user=obj.user)
        return OrderSerializer(mealorders, many=True).data

        
class OrderSerializer(serializers.ModelSerializer):
    mealorders = MealOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id","mealorders"]