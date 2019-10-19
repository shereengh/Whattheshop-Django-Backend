from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Meal, Order, MealOrder
from .serializers import MealSerializer, UserCreateSerializer, MyTokenObtainPairSerializer, MealOrderSerializer
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
        print(MealOrder.objects.all())
        return Response([request.data]) 