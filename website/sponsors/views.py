from django.shortcuts import render, HttpResponse
from sponsors.models import *
from esummit.models import Year_Detail

# Create your views here.
def sponsors(request):
    esummit = Esummit.objects.all().order_by('-year')
    events = Event.objects.all()
    sponsors = Sponsor.objects.all()
    context = {}
    year = Year_Detail.objects.all().order_by("-year")
    context['years'] = year
    max_year=0
    max_id=0
    for y in Year_Detail.objects.all():
        if(y.year>max_year):
            max_year=y.year
            max_id=y.id
    context['latest'] = max_id
    context['latest_year'] = max_year%100
    context['esummit'] = esummit
    context['events'] = events
    context['sponsors'] = sponsors
    return render(request, 'sponsors/sponsors.html',context)
