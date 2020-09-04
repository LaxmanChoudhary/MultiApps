import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class TaskGroup(models.Model):
	name = models.CharField(max_length=128)
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class Task(models.Model):
	title = models.CharField(max_length=256)
	text = models.TextField(blank=True, null=True)
	task_group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	completed = models.BooleanField(default=False)
	creator = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name="todo_created_by",
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["created_on", "title"]