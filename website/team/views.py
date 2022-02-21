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
    year = timezone.now().date().year
    if timezone.now().date().month < 6:
        year -= 1
    
    third_year= Members.objects.filter(passing_out_date__gte=timezone.now().date()).filter(passing_out_date__year = year + 2).order_by('name')
    second_year=Members.objects.filter(passing_out_date__gte=timezone.now().date()).filter(passing_out_date__year = year + 3).order_by('name')

    position_holders=[]

    for member in Members.objects.filter(passing_out_date__gte=timezone.now().date()).filter(position='President'):
        position_holders.append(member)
    for member in Members.objects.filter(passing_out_date__gte=timezone.now().date()).filter(position='General Secretary'):
        position_holders.append(member)
    for member in Members.objects.filter(passing_out_date__gte=timezone.now().date()).filter(position='Treasurer'):
        position_holders.append(member)
    for member in Members.objects.filter(passing_out_date__gte=timezone.now().date()).filter(position='Vice President'):
        position_holders.append(member)
    for member in Members.objects.filter(passing_out_date__gte=timezone.now().date()).filter(position='Convenor'):
        position_holders.append(member)
    for member in Members.objects.filter(passing_out_date__gte=timezone.now().date()).filter(passing_out_date__year = year + 1).exclude(position='President').exclude(position='Vice President').exclude(position='General Secretary').exclude(position='Convenor').exclude(position='Treasurer'):
        position_holders.append(member)

    # print(position_holders)

    context['final']=position_holders
    context['third']=[third for third in third_year]
    context['second']=[second for second in second_year]
    alumni_dic = dict()
    alumni_list = Members.objects.filter(passing_out_date__lt=timezone.now().date()).order_by('name')
    starting_year=timezone.now().date().year
    while starting_year>1990:
        current_year_alumni = alumni_list.filter(passing_out_date__year=starting_year).order_by('name')
        if current_year_alumni.count() == 0:
            starting_year-=1
        else:
            current_list = []
            for alumnus in current_year_alumni:
                current_list.append(alumnus)
            alumni_dic[starting_year]=current_list 
            starting_year-=1
    context['alumni_dic'] = alumni_dic
    year_list=[0]
    for year in alumni_dic:
        year_list.append(year)
    max_year = max(year_list)
    context['max_alumni_year'] = max_year
    print(max_year)
    return render(request,'team/team_page.html',context)
