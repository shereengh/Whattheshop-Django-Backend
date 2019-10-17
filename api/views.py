from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Meal
from .serializers import MealSerializer, UserCreateSerializer, MyTokenObtainPairSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class MealList(ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


