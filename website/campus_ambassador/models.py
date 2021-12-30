from django.db import models
from django.utils import timezone
# Create your models here.
# Models for home page
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