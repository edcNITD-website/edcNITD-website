from django.db import models

# Create your models here.

class Members(models.Model):
    name=models.CharField(max_length=100,default=None)
    position= models.CharField(blank=True,max_length=100,default=None)
    image=models.ImageField(blank=True, upload_to='memberImages/',default=None)
    facebook=models.URLField(blank=True,max_length=200,default=None)
    linkedin=models.URLField(blank=True,max_length=200,default=None)
    email=models.EmailField(blank=True,max_length=254,default=None)
    passing_out_date=models.DateField(blank=False)
    # order = models.IntegerField(default=-1)
    
    def __str__(self):
        return self.name
