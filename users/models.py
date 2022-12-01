from django.contrib.auth.models import AbstractUser
from django.db import models




class User(models.Model):
    first_name = models.CharField('First_name', max_length=200)
    last_name = models.CharField('Last_name', max_length=200)
    user_name = models.CharField('User_name', max_length=50)
    email = models.CharField('Email', max_length=100)
    phone = models.CharField('Phone', max_length=50)
    password = models.CharField('Password', max_length=50)

    def __str__(self):
        return self.user_name
