from django.shortcuts import render
from .models import Members
from django.utils import timezone
from datetime import date
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
    alumni_dic = dict()
    alumni_list = Members.objects.filter(passing_out_date__lt=timezone.now().date())
    print(alumni_list)
    starting_year=timezone.now().date().year
    while starting_year>1990:
        current_year_alumni = alumni_list.filter(passing_out_date__year=starting_year)
        print(current_year_alumni)
        if current_year_alumni.count() == 0:
            starting_year-=1
        else:
            current_list = []
            for alumnus in current_year_alumni:
                current_list.append(alumnus)
            alumni_dic[starting_year]=current_list 
            starting_year-=1
    context['alumni_dic'] = alumni_dic
    print(alumni_dic)
    print(context)
    return render(request,'team/team_page.html',context)
