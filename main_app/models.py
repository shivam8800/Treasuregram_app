from django.db import models

class Treasure(models.Model):	
	name = models.CharField("Name",max_length=100)
	value = models.DecimalField("Value", max_digits=10, decimal_places=2)
	material = models.CharField("Material", max_length=100)
	location = models.CharField("Location", max_length=100)
	image = models.CharField('Image', max_length=1000)


	def __str__(self):
		return self.name
