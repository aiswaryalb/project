from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=250)
	content=models.TextField(default="")
	date=models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=50, null = True, blank = True)