from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Meal, Order, MealOrder, Profile
from .serializers import MealSerializer, UserCreateSerializer, MyTokenObtainPairSerializer, MealOrderSerializer, ProfileSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
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
        serializer = OrderSerializer(order, context={"request": request})
        # Add status
        return Response(serializer.data)
       
       
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        profile = request.user.profile
        profile_serializer = ProfileSerializer(profile, context={"request": request})
        return Response(profile_serializer.data)

    def put(self, request): 
        profile = Profile.objects.get(user=self.request.user)
        #profile = request.user.profile
        serializer = ProfileSerializer(data=request.data, instance=profile)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

