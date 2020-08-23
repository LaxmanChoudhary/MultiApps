from django.db import models
from django.conf import settings
# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Topic(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=128)
    description = models.TextField(default="")
    boards = models.ForeignKey(Board, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return 'Topic: {} | Board: {} | created: {}'.format(self.name, self.boards, self.date)