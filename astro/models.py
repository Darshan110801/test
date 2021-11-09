from django.db import models
from datetime import datetime

class Prev30(models.Model):
    date = models.CharField(max_length=11, default='')
    url = models.TextField(default='')
    explanation = models.TextField(default='')
    title = models.TextField(default='')


class astronomers(models.Model):
    name = models.CharField(max_length=1000, default='')
    image_link = models.TextField()
    yob = models.IntegerField(default=0)
    yod = models.IntegerField(default=0)
    books = models.JSONField(default='')
    info = models.TextField(default='')
