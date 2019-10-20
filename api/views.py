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
        list_of_orders = request.data
        user=self.request.user
        order = Order(user=user)
        order.save()
        for i in list_of_orders:
             meal = Meal.objects.get(id=i["meal"])
             quantity = i['quantity']
             meal_order = MealOrder(meal=meal, quantity=quantity,order=order)
             meal_order.save()
        serializer_class = MealOrderSerializer
        return Response(serializer_class.data,status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfile(ListAPIView):
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]
	def get_queryset(self):
		return Profile.objects.filter(user=self.request.user)

