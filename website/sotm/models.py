from typing import List
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FAQ(models.Model):
    question = models.CharField('Question',max_length=200)
    answer = models.TextField()
    is_hero = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.question

class Position(models.Model):
    LEVELS = (
        ('expert','expert'),
        ('amateur','amateur'),
        ('beginner','beginner'),
    )
    name = models.CharField("Position Name",max_length=200)
    level = models.CharField("Expertise level",choices=LEVELS,default=LEVELS[2],max_length=20)
    def __str__(self) -> str:
        return self.name
class Company(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    vision = models.TextField(default="")
    company_name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    positions = models.ManyToManyField(Position,blank=True)
    founders = models.CharField(max_length=200)
    founding_year = models.IntegerField()
    verified = models.BooleanField(default=False)
    is_sotm = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.company_name