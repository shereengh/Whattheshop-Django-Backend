from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Meal(models.Model):
	name = models.CharField(max_length=50)
	price= models.DecimalField(max_digits=6, decimal_places=3)
	description = models.TextField()
	img = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.name
  

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
	timestamp = models.DateTimeField(auto_now_add=True)

	def total(self):
		return sum([meal_order.total() for meal_order in self.mealorders.all()])


class MealOrder(models.Model):
	meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='mealorders')
	quantity = models.PositiveIntegerField()
	order= models.ForeignKey(Order,on_delete=models.CASCADE, related_name='mealorders')

	def total(self):
		return self.meal.price * self.quantity


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pic = models.ImageField(blank=True, null=True)
	contact = models.CharField(max_length=100,blank=True, null=True)
	
	def __str__(self):
		return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

