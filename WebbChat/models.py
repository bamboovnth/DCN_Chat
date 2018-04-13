from django.db import models


class User(models.Model):
    """
    init models user
    """
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    gifted = models.CharField(max_length=250)
    hobby = models.CharField(max_length=250)
    desire = models.CharField(max_length=250)



# Create your models here.
