from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Products(models.Model):
	p_name = models.CharField(max_length=35)
	p_descript = models.TextField(max_length=200)

class Login(models.Model):
	p_name = models.CharField(max_length=35)
	p_descript = models.TextField(max_length=200)