from django.db import models
from django.utils import timezone
# Create your models here.

class Contributors(models.Model):
    name=models.CharField(max_length=100,default=None)
    image=models.ImageField(blank=True, upload_to='memberImages/',default=None)
    github=models.URLField(blank=True,max_length=200,default=None)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contributors'
