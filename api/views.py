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
        serializer = OrderSerializer(order)
        # Add status
        return Response(serializer.data)
       
       
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = request.user.profile
        except:
            pass
        else:
            profile_serializer = ProfileSerializer(profile, context={"request": request})
        return Response(profile_serializer.data)
