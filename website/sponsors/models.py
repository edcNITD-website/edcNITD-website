from django.db import models

# Create your models here.


class Sponsor(models.Model):
    sponsor_image = models.ImageField(
        upload_to='sponsorImage/', default=None)
    sponsor_name = models.CharField(max_length=100)
    sponsor_order = models.IntegerField(default=1)
    sponsor_website = models.URLField(default='#')

    def __str__(self) -> str:
        return self.sponsor_name


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    event_description = models.TextField(max_length=1200)
    event_sponsors = models.ManyToManyField(Sponsor)
    event_order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.event_name


# THIS IS BEING USED FOR TITLE SPONSORS


class EsummitSponsor(models.Model):
    image = models.ImageField(
        upload_to='EsponsorImage/', default=None)
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=1)
    website = models.TextField(default='#')
    type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


# THIS IS BEING USED IN CAROUSEL
class Esummit(models.Model):
    year = models.IntegerField(default=2023)
    esummit_image = models.ImageField(
        blank=True, upload_to='esummitImage/', default=None)
    esummit_sponsors = models.ManyToManyField(EsummitSponsor)

    def __str__(self) -> str:
        return str(self.year)


# BROCHURE DOWNLOAD

class Brochure(models.Model):
    brochure = models.FileField(upload_to='brochurePDF')
