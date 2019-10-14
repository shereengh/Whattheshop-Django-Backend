from django.db import models

class Meal(models.Model):
	name = models.CharField(max_length=50)
	price= models.DecimalField(max_digits=6, decimal_places=3)
	description = models.TextField()
	img = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.name

