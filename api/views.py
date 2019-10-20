from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Meal, Order, MealOrder, Profile
from .serializers import MealSerializer, UserCreateSerializer, MyTokenObtainPairSerializer, MealOrderSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class MealList(ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class Checkout(APIView):
    def post(self, request, format=None):
        order_list = request.data
        user = request.user
        order = Order.objects.create(user=user)
        for order_item in order_list:
             MealOrder.objects.create(
                meal_id=order_item["meal"],
                quantity=order_item['quantity'],
                order=order
            )
        # serializer_class = MealOrderSerializer
        return Response([])
        # return Response(serializer_class.data,status=status.HTTP_200_OK)
        # return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        profile = Profile.objects.get(user=request.user)
        serializer_class = ProfileSerializer(profile)
        return Response(serializer_class.data)
        
		

   