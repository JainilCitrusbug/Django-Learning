from operator import mod
from statistics import mode
from tkinter import Widget
from unicodedata import name
from django.db import models

# Create your models here.

class student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=70)
    course = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class info(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    course = models.CharField(max_length=70)

    def __str__(self):
        return self.name