from django.shortcuts import render
from .models import Contributors
from esummit.models import Year_Detail

# Create your views here.

def web_team(request):
    context={
        'contributors':Contributors.objects.all().order_by('name')
    }
    ordering=['date']
    
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
    return render(request,'web_team/web_team.html',context)

