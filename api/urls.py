from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserCreateAPIView, MealList

urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('meals/', MealList.as_view(), name="meal-list" ),
]