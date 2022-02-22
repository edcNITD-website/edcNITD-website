from django.db import models

# Create your models here.

class Year_Detail(models.Model):
    year = models.IntegerField()
    year_img = models.ImageField(
        blank=True, upload_to='esummitYear/', default=None)
    year_desc = models.TextField(default="")
    yt_link = models.URLField(max_length=200,default=None)
    
    def __str__(self) -> str:
        return str(self.year)
    
    
class Carousel(models.Model):
    year = models.ForeignKey(Year_Detail, on_delete=models.CASCADE)
    event_img = models.ImageField(
        blank=True, upload_to='esummitSlider/', default=None)
    title = models.CharField(max_length=500, default=None)
    subtitle = models.TextField(default="")
    btn_content = models.CharField(max_length=200, default=None)
    btn_link = models.CharField(max_length=200, default=None)
    is_hero = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.year.year)+"_"+self.title
    

class Event(models.Model):
    year = models.ForeignKey(Year_Detail, on_delete=models.CASCADE)
    event_img = models.ImageField(
        blank=True, upload_to='esummitEvents/', default=None)
    event_title = models.CharField(max_length=500, default=None)
    event_detail = models.TextField(default="")
    
    def __str__(self) -> str:
        return str(self.year.year)+"_"+self.event_title
    
    
class Speaker(models.Model):
    year = models.ForeignKey(Year_Detail, on_delete=models.CASCADE)
    speaker_img = models.ImageField(
        blank=True, upload_to='esummitSpeakers/', default=None)
    speaker_title = models.CharField(max_length=500, default=None)
    speaker_subtitle = models.TextField(default="")
    speaker_desc = models.TextField(default="")
    
    def __str__(self) -> str:
        return str(self.year.year)+"_"+self.speaker_title
    
    
class Glimpse(models.Model):
    year = models.ForeignKey(Year_Detail, on_delete=models.CASCADE)
    glimpse_img = models.ImageField(
        blank=True, upload_to='esummitGlimpses/', default=None)
    glimpse_desc = models.CharField(max_length=100, default=None)
    
    def __str__(self) -> str:
        return str(self.year.year)+"_"+self.glimpse_desc