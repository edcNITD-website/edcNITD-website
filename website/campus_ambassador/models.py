from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
# Create your models here.
def urlChecker(url_string) ->str:
    if 'https://' not in url_string:
        url_string = "https://"+url_string
    return url_string
# Models for home pae
# todo Incentive, Responsibility, TimeLine, FAQ
class Incentive(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    icon_class = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.title

class Responsibliity(models.Model):
    img_url = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Responsiblities'

class TimeLineEvent(models.Model):
    deadline = models.DateTimeField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    @property
    def completed(self):
        return self.deadline<timezone.now()

    def __str__(self) -> str:
        return self.title

class FAQ(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class Ambassador(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    college = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    unique_code = models.CharField(max_length=8,default=get_random_string(8))
    score = models.IntegerField(default=0)
    facebook = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    linkedin = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    instagram = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    def __str__(self) -> str:
        return self.user.username

    def check_urls(self):
        self.facebook = urlChecker(self.facebook)
        self.linkedin = urlChecker(self.linkedin)
        self.instagram = urlChecker(self.instagram)
        self.save()
class CAPModerator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    unique_code = models.CharField(max_length=8,default=get_random_string(8))
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username