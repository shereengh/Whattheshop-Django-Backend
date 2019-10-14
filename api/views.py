from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView

from .models import Meal
from .serializers import MealSerializer, UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class MealList(ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
