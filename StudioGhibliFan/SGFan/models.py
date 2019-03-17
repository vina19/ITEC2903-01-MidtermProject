from django.db import models

#Put what data we want in database
#class SGMovies inherit from models.Model
class SGMovies(models.Model):
	title = models.CharField(max_length = 100)
	image = models.ImageField()
	description = models.CharField(max_length=5000)
	director = models.CharField(max_length = 100)
	producer = models.CharField(max_length = 100)

	def __str__(self):
		return self.title
