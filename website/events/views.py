from django.shortcuts import render
from .models import*
import datetime

def event(request):
    
    day=datetime.datetime.now()
    tdelta=datetime.timedelta(days=45)


    ongoing_event=Event.objects.filter(start_date__lte=day,end_date__gte=day)
    upcoming_event=Event.objects.filter(start_date__gte=day,end_date__lte=day+tdelta).exclude(start_date__lte=day,end_date__gte=day)
    all_event=Event.objects.all()

    oe_count=0
    ue_count=0
    ae_count=0
    
    if Event.objects.filter(start_date__lte=day,end_date__gte=day).count()>0:
        oe_count=1
    
    if Event.objects.filter(start_date__gte=day,end_date__lte=day+tdelta).exclude(start_date__lte=day,end_date__gte=day).count()>0:
        ue_count=1

    if Event.objects.count()>0:
        ae_count=1


    context={'ue':upcoming_event,'oe':ongoing_event,'ae':all_event,'ae_count':ae_count,'ue_count':ue_count ,'oe_count':oe_count}

    return render(request,'events/event_page.html', context)