from django.db import models
from django.contrib.auth.models import User


class Meal(models.Model):
	name = models.CharField(max_length=50)
	price= models.DecimalField(max_digits=6, decimal_places=3)
	description = models.TextField()
	img = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')


class MealOrder(models.Model):
	meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='mealorder')
	quantity = models.PositiveIntegerField()
	order= models.ForeignKey(Order,on_delete=models.CASCADE, related_name='mealorder')