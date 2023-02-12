from operator import mod
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

class SecretKey(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=10,default=uuid.uuid4().hex[:10])
    def __str__(self) -> str:
        return self.name
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

# todo campaign
class Campaign(models.Model):
    start_date = models.DateTimeField();
    end_date = models.DateTimeField();
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    campaign = models.ForeignKey(Campaign,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    description = models.TextField()
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
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
    def index(self):
        result = str(self.task.number)+'.'+str(self.number)
        return result

class Avatar(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.name

class Ambassador(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img = models.CharField(max_length=300,default='default.png')
    campaign = models.ForeignKey(Campaign,on_delete=models.CASCADE)
    has_completed = models.BooleanField(default=False)
    college = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    completed_prog = models.BooleanField(default=False)
    unique_code = models.CharField(max_length=20,default=uuid.uuid4().hex[:8])
    score = models.IntegerField(default=0)
    subtasks_completed = models.TextField(default='',blank=True)
    facebook = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    linkedin = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    instagram = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    active = models.BooleanField(default=False)
    drive_link = models.CharField(max_length=400,default='Pending')
    def __str__(self) -> str:
        return self.user.username

    def check_urls(self):
        self.facebook = urlChecker(self.facebook)
        self.linkedin = urlChecker(self.linkedin)
        self.instagram = urlChecker(self.instagram)
        self.save()
    
    @property
    def get_all_subtasks(self):
        all_subtasks = SubTask.objects.all().order_by('task__number','number')
        # print(all_subtasks)
        result = []
        for st in all_subtasks:
            completed_st_ids = self.subtasks_completed.split('|')
            if str(st.id) in completed_st_ids:
                new_st = st
                new_st.completed = True
            else:
                new_st = st
                new_st.completed = False
            result.append(new_st)
        return result

    @property
    def get_current_task(self):
        all_tasks = Task.objects.filter(campaign=self.campaign).order_by('start_date')
        task_list = []
        for task in all_tasks:
            if task.start_date<=timezone.now() and task.end_date >=timezone.now():
                task_list.append(task)
        if len(task_list) == 0:
            return None
        else:
            return task_list[len(task_list)-1]
        return None

    @property
    def get_ongoing_tasks(self):
        all_tasks = Task.objects.filter(campaign=self.campaign).order_by('-start_date')
        ongoing_tasks = []
        for task in all_tasks:
            if task.start_date<=timezone.now() and task.end_date >=timezone.now():
                if task != self.get_current_task:
                    new_task = task
                    new_task.subtasks = SubTask.objects.filter(task=task).order_by('number')
                    ongoing_tasks.append(new_task)
        if len(ongoing_tasks) == 0:
            return None
        return ongoing_tasks

    @property
    def get_all_current_subtasks(self):
        all_subtasks = SubTask.objects.filter(task=self.get_current_task).order_by('number')
        return all_subtasks


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