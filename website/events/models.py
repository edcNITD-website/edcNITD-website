from django.db import models

class UpcomingEvent(models.Model):
    event_name=models.CharField(max_length=15)
    about_event=models.TextField()
    image1=models.ImageField(upload_to=None, default="")

    def __str__(self):
        return self.event_name

class OtherEvent(models.Model):
    eventname=models.CharField(max_length=15)
    aboutevent=models.TextField()
    img1=models.ImageField(upload_to=None, default="")

    def __str__(self):
        return self.eventname