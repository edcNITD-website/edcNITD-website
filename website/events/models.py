from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, datetime, tzinfo
import pytz

class Event(models.Model):
    event_name=models.CharField(max_length=100)
    about_event=models.TextField(max_length=1200)
    prizes=models.TextField(max_length=1000,default="",blank=True,null=True)
    poster=models.ImageField(upload_to='events/', default="",blank=True,null=False)
    start_date=models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    end_date=models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    registration_link=models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name_plural = 'Events'

class EventImages(models.Model):
    event=models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    images=models.FileField(upload_to='events/', default="",blank=True,null=False)

    def __str__(self):
        return self.event.event_name

    class Meta:
        verbose_name_plural = 'Event Images'

class Timeline(models.Model):
    event=models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    date_event=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    details=models.CharField(max_length=300)

    def __str__(self):
        return self.event.event_name + " " + self.title

    @property
    def is_past_due(self):
        tz = pytz.timezone('UTC')
        date_check = datetime.now(tz)
        return date_check > self.date_event
    class Meta:
        verbose_name_plural = 'Timeline'
        ordering=('date_event',)

