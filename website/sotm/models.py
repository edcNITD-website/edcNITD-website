from datetime import timedelta
from typing import List
from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.expressions import Random
from website import settings
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your models here.

def urlChecker(url_string) ->str:
    if 'https://' not in url_string:
        url_string = "https://"+url_string
    return url_string


class AboutSec(models.Model):
    heading = models.CharField('About-Heading', max_length=200)
    content = models.TextField()

    def __str__(self) -> str:
        return self.heading

class FAQ(models.Model):
    question = models.CharField('Question', max_length=200)
    answer = models.TextField()
    is_hero = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.question


class OpportunityTag(models.Model):
    name = models.CharField("Opportunity Name", max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(
        blank=True, upload_to='companyLogos/', default=None)
    vision = models.TextField(default="")
    company_name = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=20)
    domain = models.CharField(max_length=100)
    founders = models.CharField(max_length=200)
    founding_year = models.IntegerField()
    verified = models.BooleanField(default=False)
    is_sotm = models.BooleanField(default=False)
    facebook = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    linkedin = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    instagram = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    website = models.CharField(
        max_length=200, null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = 'Companies'

    def new_registeration(self):
        # todo send email to edc regarding new registeration by the company
        subject = "A new company has registered! Their name is "+self.company_name
        html_message = render_to_string('sotm/email_to_edc_registeration.html',context={'company':self})
        plain_message = strip_tags(html_message)
        send_mail(
            subject=subject,
            message=plain_message,
            html_message=html_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["edcnitd.official@gmail.com"],
        )
        # todo send email to company regarding their registeration
        subject = "Registeration in Startup of the Month, EDC NIT Durgapur"
        html_message = render_to_string('sotm/email_to_company_registeration.html',context={'company':self})
        plain_message = strip_tags(html_message)
        send_mail(
            subject=subject,
            message=plain_message,
            html_message=html_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
        )

    def __str__(self) -> str:
        return self.company_name

    def positions(self) -> List:
        result = Opportunity.objects.filter(company=self)
        return result

    def has_position(self, position_name):
        positon_names = []
        for position in self.positions().all():
            positon_names.append(position.name)
        for name in positon_names:
            if name == position_name:
                return True
        return False

    def get_opportunities(self) -> List:
        opportunities = Opportunity.objects.filter(company=self)
        return opportunities

    def save(self):
        self.facebook = urlChecker(self.facebook)
        self.linkedin = urlChecker(self.linkedin)
        self.website = urlChecker(self.website)
        self.instagram = urlChecker(self.instagram)
        super(Company, self).save()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_dp = models.ImageField(
        blank=True, upload_to='studentDp/', default=None,null=True)
    facebook = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    linkedin = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    instagram = models.CharField(
        max_length=200, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return self.user.username

    def save(self):
        self.facebook = urlChecker(self.facebook)
        self.linkedin = urlChecker(self.linkedin)
        self.instagram = urlChecker(self.instagram)
        super(Student, self).save()

class Opportunity(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField("Opportunity Name", max_length=200)
    tags = models.ManyToManyField(OpportunityTag)
    register_url = models.CharField("Link to register", max_length=300)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return str(self.company)+" | "+self.name

    class Meta:
        verbose_name_plural = 'Opportunities'

class TemporaryLink(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    exp_timestamp = models.DateTimeField(default=timezone.now)
    key = models.CharField("Key",max_length=64,unique=True)
    
    def __str__(self) -> str:
        return 'otp_'+self.user.username
    def generate(self) -> None:
        self.key = get_random_string(64)
        currrent_time = timezone.now()
        print(currrent_time)
        exp_time = currrent_time+timedelta(seconds=3600)
        print(exp_time)
        self.exp_timestamp = exp_time
        self.save()
    def send(self):
        send_mail(
            subject="Change password request for Startup of the Month",
            message="Change password request for Startup of the Month. The Link remains valid for 1 hour only. Please click on the link below to change you password 'https://edcnitd.co.in/sotm/key/"+self.key+"/'",
            html_message="Change password request for Startup of the Month. The Link remains valid for 1 hour only. Please click on the link below to change you password <br> <a href='https:/edcnitd.co.in/sotm/key/"+self.key+"/'>click here</a>",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
        )
