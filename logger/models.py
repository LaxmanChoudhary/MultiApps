from django.db import models

# Create your models here.
class Board(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Topic(models.Model):
	date = models.DateField()
	name = models.CharField(max_length=128)
	description = models.TextField(default="")
	boards  = models.ForeignKey(Board, on_delete=models.CASCADE)

	def __str__(self):
		return 'Topic: {} | Board: {} | created: {}'.format(self.name, self.boards, self.date)