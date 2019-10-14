from rest_framework.generics import CreateAPIView
from .serializers import MealSerializer, UserCreateSerializer, LoginSerializer

from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView

from .models import Meal
####################################################

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

###############################################

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = LoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

#######################################################################

class MealList(ListAPIView):
	serializer_class = MealSerializer
	def get_queryset(self):
		return Meal.objects.all()

##############################################