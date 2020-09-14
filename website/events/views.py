from django.shortcuts import render
from .models import*
import datetime

def event(request):
    month= datetime.datetime.now().month
    day= datetime.datetime.now().day

    ongoing_event=Event.objects.filter(current_day=day)
    upcoming_event=Event.objects.filter(current_month=month,current_day__range=[day,31]).exclude(current_day__range=[day,day])
    all_event=Event.objects.all()

    oe_count=0
    ue_count=0
    ae_count=0
    
    if Event.objects.filter(current_day=day).count()>0:     
        oe_count=1
    
    if Event.objects.filter(current_month=month,current_day__range=[day,31]).exclude(current_day__range=[day,day]).count()>0:
        ue_count=1

    if Event.objects.count()>0:
        ae_count=1


    context={'ue':upcoming_event,'oe':ongoing_event,'ae':all_event,'ae_count':ae_count,'ue_count':ue_count ,'oe_count':oe_count}

    return render(request,'events/event_page.html', context)