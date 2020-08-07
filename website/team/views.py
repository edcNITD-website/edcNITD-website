from django.shortcuts import render
from .models import Members

# Create your views here.

def team(request):
    members=Members.objects.all()
    context={}
    # names=[member.name for member in members]
    # year=[member.year for member in members]
    # images=[member.image for member in members]
    positions=[member.position for member in Members.objects.all()]
    
    third_year= Members.objects.filter(year=3).order_by('name')
    second_year=Members.objects.filter(year=2).order_by('name')

    position_holders=[]

    for member in Members.objects.filter(position='President'):
        position_holders.append(member)
    for member in Members.objects.filter(position='General Secretary'):
        position_holders.append(member)
    for member in Members.objects.filter(position='Treasurer'):
        position_holders.append(member)
    for member in Members.objects.filter(position='Vice President'):
        position_holders.append(member)
    for member in Members.objects.filter(position='Convenor'):
        position_holders.append(member)
    for member in Members.objects.filter(year=4).exclude(position='President').exclude(position='Vice President').exclude(position='General Secretary').exclude(position='Convenor').exclude(position='Treasurer'):
        position_holders.append(member)

    # print(position_holders)

    context['final']=position_holders
    context['third']=[third for third in third_year]
    context['second']=[second for second in second_year]
    
    return render(request,'team/team_page.html',context)
