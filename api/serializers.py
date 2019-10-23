from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Meal, MealOrder, Profile, Order
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        profile= Profile.objects.get(user=new_user)
        profile.contact= self.context['request'].data['contact']
        profile.save()
        return validated_data


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        return token


class MealOrderSerializer(serializers.ModelSerializer):
    meal = MealSerializer()
    class Meta:
        model = MealOrder
        fields = ["meal","quantity"]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UpdateUserSerializer()
    orders_list = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["user","pic","contact","orders_list"]

    def get_orders_list(self, obj):
        mealorders = Order.objects.filter(user=obj.user)
        return OrderSerializer(mealorders, many=True).data


    def update(self, instance, validated_data):
        profile_data = validated_data.pop('user')
        print ("last_name",instance.user.last_name)
        instance.user.first_name = profile_data.get('first_name', profile_data['first_name'])
        instance.user.last_name = profile_data.get('last_name', profile_data['last_name'])
        instance.user.email = profile_data.get('email', profile_data['email'])
        instance.contact = validated_data.get('contact', instance.contact)
        instance.pic = validated_data.get('pic', instance.pic)
        print ("last_name",instance.user.last_name)
        print("first_name",instance.user.first_name)
        print("email",instance.user.email)
        instance.user.save()
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    mealorders = MealOrderSerializer(many=True)
    total = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ["id","total","timestamp","mealorders"]

    def get_total(self, obj):
        return obj.total()


