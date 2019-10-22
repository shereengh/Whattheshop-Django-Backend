from django.contrib import admin
from .models import Meal, Order, MealOrder, Profile


class MealOrderInline(admin.TabularInline):
	model = MealOrder

class OrderAdmin(admin.ModelAdmin):
	inlines = [
	    MealOrderInline,
	]
admin.site.register(Meal)
admin.site.register(Order, OrderAdmin)
admin.site.register(Profile)