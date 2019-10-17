from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserCreateAPIView, MealList, MyTokenObtainPairView, UserProfile

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('meals/', MealList.as_view(), name="meal-list" ),
    path('userprofile/', UserProfile.as_view(), name="user-profile" ),

]