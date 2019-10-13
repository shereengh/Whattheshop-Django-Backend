from django.urls import path
from .views import UserCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
################################################################

# app_name="api"

urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]