from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Event(models.Model):
    event_name=models.CharField(max_length=15)
    about_event=models.TextField(max_length=500)
    image=models.ImageField(upload_to=None, default="",blank=True,null=False)
    event_month=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(12)])
    start_date=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(31)])
    end_date=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(31)])
    
    def __str__(self):
        return self.event_name