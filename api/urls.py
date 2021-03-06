from django.urls import path
from .views import UserCreateAPIView, MealList, MyTokenObtainPairView, Checkout,  UserProfile


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('meals/', MealList.as_view(), name="meal-list" ),
    path('checkout/', Checkout.as_view(), name="checkout" ),
    path('profile/', UserProfile.as_view(), name="profile" ),
]