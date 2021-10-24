from typing import List
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FAQ(models.Model):
    question = models.CharField('Question',max_length=200)
    answer = models.TextField()
    is_hero = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.question

class Position(models.Model):
    name = models.CharField("Position Name",max_length=200,unique=True)
    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    logo=models.ImageField(blank=True, upload_to='companyLogos/',default=None)
    vision = models.TextField(default="")
    company_name = models.CharField(max_length=100)
    company_phone = models.IntegerField()
    domain = models.CharField(max_length=100)
    positions = models.ManyToManyField(Position,blank=True)
    founders = models.CharField(max_length=200)
    founding_year = models.IntegerField()
    verified = models.BooleanField(default=False)
    is_sotm = models.BooleanField(default=False)
    facebook = models.CharField(max_length=200,null=True,blank=True,default=None)
    linkedin = models.CharField(max_length=200,null=True,blank=True,default=None)
    instagram = models.CharField(max_length=200,null=True,blank=True,default=None)
    website = models.CharField(max_length=200,null=True,blank=True,default=None)
    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return self.company_name

    def add_position(self,position_name):
        position = Position.objects.filter(name=position_name).first()
        self.positions.add(position)
        self.save()
        
    def remove_position(self,position_name):
        position = Position.objects.filter(name=position_name).first()
        self.positions.remove(position)
        self.save()

    def has_position(self,position_name):
        positon_names = []
        for position in self.positions.all():
            positon_names.append(position.name)
        for name in positon_names:
            if name == position_name:
                return True
        return False
    
    def get_opportunities(self) -> List:
        opportunities = Opportunity.objects.filter(company=self)
        return opportunities
        
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.username

class Opportunity(models.Model):
    company= models.ForeignKey(Company,on_delete=models.CASCADE)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
    register_url = models.CharField("Link to register",max_length=300)
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.company)+'_'+str(self.position)

    class Meta:
        verbose_name_plural = 'Opportunities'