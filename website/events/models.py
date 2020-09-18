from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Event(models.Model):
    event_name=models.CharField(max_length=15)
    about_event=models.TextField(max_length=500)
    image=models.ImageField(upload_to=None, default="",blank=True,null=False)
    start_date=models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    end_date=models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    registration_link=models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.event_name