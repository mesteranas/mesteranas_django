from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    arabicTitle=models.CharField(max_length=500)
    englishTitle=models.CharField(max_length=500)
    arabicBody=models.TextField()
    englishBody=models.TextField()
    date=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.englishTitle
class Comments(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    post=models.ForeignKey(to=post,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    content=models.TextField()
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title