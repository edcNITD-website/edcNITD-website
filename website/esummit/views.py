from django.shortcuts import render
from django.shortcuts import get_object_or_404
from esummit.models import *


def esummit(requests, year_id):
    year_detail = Year_Detail.objects.all().order_by("-year")
    esumInfo = {}
    esumInfo['years'] = year_detail
    max_year=0
    max_id=0
    for y in Year_Detail.objects.all():
        if(y.year>max_year):
            max_year=y.year
            max_id=y.id
    esumInfo['latest'] = max_id
    esumInfo['latest_year'] = max_year%100
    year = get_object_or_404(Year_Detail, id=year_id)
    events = Event.objects.filter(year=year)
    speakers = Speaker.objects.filter(year=year)
    glimpses = Glimpse.objects.filter(year=year)
    esumInfo['year'] = year
    esumInfo['active_slider'] = Carousel.objects.filter(is_hero=True,year=year)
    esumInfo['slider'] = Carousel.objects.filter(is_hero=False,year=year)
    esumInfo['events'] = events
    esumInfo['speakers'] = speakers
    esumInfo['glimpses'] = glimpses
    return render(requests,'esummit/esummit_page.html', esumInfo)
