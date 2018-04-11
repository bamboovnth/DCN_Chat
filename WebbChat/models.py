from django.db import models


class User(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    gifted = models.CharField(max_length=50)
    hobby = models.CharField(max_length=50)
    desire = models.CharField(max_length=50)


# Create your models here.
