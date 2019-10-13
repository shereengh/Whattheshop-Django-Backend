from rest_framework.generics import CreateAPIView
from .serializers import MealSerializer,UserCreateSerializer

from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView

from .models import Meal

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class MealList(ListAPIView):
	serializer_class = MealSerializer
	def get_queryset(self):
		return Meal.objects.all()

