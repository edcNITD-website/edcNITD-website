from django.shortcuts import render
from campus_ambassador.models import *
# Create your views here.
def home(request):
    context = {}
    incentives = Incentive.objects.all().order_by('title')
    responsibilities = Responsibliity.objects.all().order_by('title')
    timeline = TimeLineEvent.objects.all().order_by('deadline')
    context['incentives'] = incentives
    context['responsibilities'] = responsibilities
    context['timeline'] = timeline
    context['faqs'] = FAQ.objects.filter(active=False).order_by('title')
    context['active_faqs'] = FAQ.objects.filter(active=True).order_by('title')
    print(context)
    return render(request,'campus_ambassador/home.html',context)