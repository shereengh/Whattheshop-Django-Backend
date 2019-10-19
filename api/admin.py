from django.contrib import admin
from .models import Meal, Order, MealOrder

admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(MealOrder)