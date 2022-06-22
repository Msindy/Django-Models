from datetime import date
from typing import Text
from webbrowser import get
from django.db import models
from django.contrib.auth import get_user_model
user=get_user_model()


# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField()
    Author = models.ForeignKey(user, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(auto_now=True)