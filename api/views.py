from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Meal, Profile
from .serializers import MealSerializer, UserCreateSerializer, MyTokenObtainPairSerializer, ProfileSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class MealList(ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserProfile(ListAPIView):
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]
	def get_queryset(self):
		return Profile.objects.filter(user=self.request.user)