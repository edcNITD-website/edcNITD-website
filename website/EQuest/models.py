from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
from django.urls import reverse
# Create post model
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    genre=models.CharField(max_length=100,default=None)
    image=models.ImageField(blank=True, upload_to=None,default=None)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
