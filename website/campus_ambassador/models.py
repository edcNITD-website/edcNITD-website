from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import uuid
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

class Task(models.Model):
    title = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    description = models.TextField()
    def __str__(self) -> str:
        return str(self.number)+' | '+ self.title

class SubTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    score = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    submission_url = models.CharField(max_length=400,default="")
    def __str__(self) -> str:
        return self.title
    @property
    def precedence(self):
        pre = 1000*self.task.number+self.number
        return pre
    @property
    def index(self):
        result = str(self.task.number)+'-'+str(self.number)
        return result
class Ambassador(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    college = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    completed_prog = models.BooleanField(default=False)
    unique_code = models.CharField(max_length=8,default=uuid.uuid4().hex[:8])
    score = models.IntegerField(default=0)
    facebook = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    linkedin = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    instagram = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    active = models.BooleanField(default=False)
    current_task = models.CharField(max_length=10,default="1-1")
    def __str__(self) -> str:
        return self.user.username

    def check_urls(self):
        self.facebook = urlChecker(self.facebook)
        self.linkedin = urlChecker(self.linkedin)
        self.instagram = urlChecker(self.instagram)
        self.save()
    
    @property
    def get_current_task(self):
        index = str()
        index = self.current_task
        task_num =  index.split('-')[0]
        return Task.objects.get(number=task_num)
    
    @property
    def get_current_subtask(self):
        index = str()
        index = self.current_task
        subtask_num =  index.split('-')[1]
        return SubTask.objects.get(number=subtask_num)
    
class CAPModerator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    unique_code = models.CharField(max_length=8,default=uuid.uuid4().hex[:8],unique=True)

    def __str__(self) -> str:
        return self.user.username

class SubTaskCompletionRequest(models.Model):
    subtask = models.ForeignKey(SubTask,on_delete=models.CASCADE)
    score_allotted = models.IntegerField(default=0)
    ambassador = models.ForeignKey(Ambassador,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.CharField(max_length=8,default=uuid.uuid4().hex[:8])
    def __str__(self) -> str:
        return self.subtask.title+' by '+self.ambassador.user.username