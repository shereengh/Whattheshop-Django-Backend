from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save


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


class Profile(models.Model):
	# switch to one to one
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profilepic = models.ImageField(blank=True, null=True)
	bio = models.TextField()
	def __str__(self):
		return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
	if kwargs.get('created', False):
		Profile.objects.get_or_create(user= kwargs.get('instance'),)

