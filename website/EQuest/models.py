from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
from django.urls import reverse
# Create post model


class Category(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    slug=models.SlugField(unique=True)
    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post:post_by_category',args=[self.slug])

    class Meta:
        verbose_name_plural = 'Category'

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(blank=True, upload_to='equest/',default=None)
    fblink=models.URLField(blank=True,default=None)
    instalink=models.URLField(blank=True,default=None)
    class Meta:
        ordering=('-date',)
        
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post:post_detail',args=[self.id,])