from django.shortcuts import render
from django.shortcuts import get_object_or_404
from esummit.models import *


def home(requests):
    year = Year_Detail.objects.all().order_by("-year")
    context = {}
    context['years'] = year
    max_year=0
    max_id=0
    for y in Year_Detail.objects.all():
        if(y.year>max_year):
            max_year=y.year
            max_id=y.id
    context['latest'] = max_id
    print(context)
    return render(requests,'forum/home_page.html', context)

def esummit(requests, year_id):
    year_detail = Year_Detail.objects.all().order_by("-year")
    context = {}
    context['years'] = year_detail
    max_year=0
    max_id=0
    for y in Year_Detail.objects.all():
        if(y.year>max_year):
            max_year=y.year
            max_id=y.id
    context['latest'] = max_id
    year = get_object_or_404(Year_Detail, id=year_id)
    events = Event.objects.filter(year=year)
    speakers = Speaker.objects.filter(year=year)
    glimpses = Glimpses.objects.filter(year=year)
    context['active_slider'] = Slider.objects.filter(is_hero=True,year=year)
    context['slider'] = Slider.objects.filter(is_hero=False,year=year)
    context['events'] = events
    context['speakers'] = speakers
    context['glimpses'] = glimpses
    return render(requests,'esummit/esummit_page.html', context)
