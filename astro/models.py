from django.db import models


class Prev30(models.Model):
    date = models.CharField(max_length=11,default='')
    url = models.TextField(default='')
    explanation = models.TextField(default='')
    title = models.TextField(default='')


