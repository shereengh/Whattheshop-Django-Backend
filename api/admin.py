from django.contrib import admin
from .models import Meal, Order, MealOrder, Profile

admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(MealOrder)
admin.site.register(Profile)