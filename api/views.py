from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Meal, Order, MealOrder, Profile
from .serializers import MealSerializer, UserCreateSerializer, MyTokenObtainPairSerializer, MealOrderSerializer, ProfileSerializer, OrderSerializer
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
        order = Order.objects.get(user=request.user)
        serializer_class = OrderSerializer(order)
        return Response(serializer_class.data)
       
       
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        profile = Profile.objects.get(user=request.user)
        # serializer_class = ProfileSerializer(profile)

        profile_serializer = ProfileSerializer(profile, context={"request": request})
        profile_serializer.data

        return Response(profile_serializer.data)
        
	


# class OrdersList(ListAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]
  
#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)
        
        # orders = Order.objects.filter(user=self.request.user)
        # serializer_class = OrderSerializer(orders)
        # return Response(serializer_class.data)



