from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(models.Model):
    first_name = models.CharField('First_name', max_length=200)
    last_name = models.CharField('Last_name', max_length=200)
    username = models.CharField('Username', max_length=50, null=True)
    email = models.CharField('Email', max_length=100)
    phone = models.CharField('Phone', max_length=50)
    password = models.CharField('Password', max_length=50)

    def __str__(self):
        return self.username


class DataMetric(models.Model):
    datametric = models.CharField('datametric', max_length=50)


    def __str__(self):
        return self.datametric


class Images(models.Model):
    title = models.CharField('title', max_length=150)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.images

