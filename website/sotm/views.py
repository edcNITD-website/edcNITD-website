from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from sotm.models import *
from django.contrib.auth.models import AnonymousUser, User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def sotm_home(request):
    context = {}
    context['hero_faqs'] = FAQ.objects.filter(is_hero=True)
    context['normal_faqs'] = FAQ.objects.filter(is_hero=False)
    verified_companies = Company.objects.filter(verified=True)
    all_opportunities = []
    count=0
    for company in verified_companies:
        for opp in Opportunity.objects.filter(company=company):
            count+=1
            if count > 5:
                break
            all_opportunities.append(opp)
    context['all_opportunities'] = all_opportunities
    return render(request,'sotm/sotm_home.html',context)


def sotm_companies(request):
    context = {}
    companies_per_page = 5
    verified_companies = Company.objects.filter(verified=True)
    paginator_obj = Paginator(verified_companies,companies_per_page)
    pageNumber = request.GET.get('page')
    try:
        pageObj = paginator_obj.get_page(pageNumber)
    except PageNotAnInteger:
        pageObj = paginator_obj.get_page(1)
    except EmptyPage:
        pageObj = paginator_obj.get_page(paginator_obj.num_pages)
    context = {}
    context['company_list'] = pageObj
    context['owned_company'] = None
    for company in Company.objects.filter(verified=True):
        if company.user == request.user:
            context['owned_company'] = company        
    return render(request,'sotm/sotm_companies.html',context)

def company_view(request,company_id):
    company = get_object_or_404(Company,id=company_id)
    context = {}
    if company.user == request.user:
        context['is_owner'] = True
    else:
        context['is_owner'] = False
    context['company'] = company
    context['opportunities'] = company.get_opportunities()
    return render(request,'sotm/company_view.html',context)

@login_required
def company_edit(request,company_id):
    company = get_object_or_404(Company,id=company_id)
    context = {}
    if company.user == request.user:
        context['is_owner'] = True
    else:
        context['is_owner'] = False
    context['company'] = company
    if request.method == 'POST':
        company.company_name = request.POST.get('company_name')
        company.vision = request.POST.get('vision')
        company.domain = request.POST.get('domain')
        company.founders = request.POST.get('founders')
        company.founding_year = request.POST.get('founding_year')
        company.company_phone = request.POST.get('company_phone')
        company.facebook = request.POST.get('facebook')
        company.linkedin = request.POST.get('linkedin')
        company.instagram = request.POST.get('instagram')
        company.website = request.POST.get('website')
        company.company_phone = request.POST.get('phone')
        if 'company_logo' in request.FILES:
            if(request.FILES['company_logo'] is not None):
                company.logo.delete()
                company.logo = request.FILES['company_logo']
        company.save()
        return redirect('/sotm/')
    return render(request,'sotm/company_edit.html',context)

@login_required
def sotm_add_opportunity(request,company_id):
    company = get_object_or_404(Company,id=company_id)
    context = {}
    positions = OpportunityTag.objects.all()
    context['positions'] = positions
    context['company'] = company
    if company.user == request.user:
        context['is_owner'] = True
    else:
        context['is_owner'] = False
    if request.method == 'POST':
        if request.user == company.user:
            opportunity = Opportunity()
            opportunity.name = request.POST.get('name')
            opportunity.register_url = request.POST.get('registeration_url')
            company.save()
            opportunity.company = company
            opportunity.description = request.POST.get('description')
            opp_tags = request.POST.getlist('position_name')
            opportunity.save()
            for opp_tag in opp_tags:
                tag = OpportunityTag.objects.get(name=opp_tag)
                opportunity.tags.add(tag)
            return redirect('/sotm/')
    return render(request,'sotm/add_opportunity.html',context)

@login_required
def sotm_remove_opportunity(request,company_id):
    company = get_object_or_404(Company,id=company_id)
    context = {}
    positions = company.positions().all()
    context['positions'] = positions
    if company.user == request.user:
        context['is_owner'] = True
    else:
        context['is_owner'] = False
    if request.method == 'POST':
        if request.user == company.user:
            company.save()
            opportunity = Opportunity.objects.filter(company=company).filter(name=request.POST.get('position_name')).first()
            opportunity.delete()
            return redirect('/sotm/')
    
    return render(request,'sotm/remove_opportunity.html',context)

@login_required
def edit_opportunity(request,company_id,opp_id):
    company = get_object_or_404(Company,id=company_id)
    opportunity = get_object_or_404(Opportunity,id=opp_id)
    context = {}
    context['company'] =company
    context['opportunity'] = opportunity
    context['positions'] = opportunity.tags.all()
    other_tags = OpportunityTag.objects.all().difference(opportunity.tags.all())
    context['other_positions'] = other_tags
    if company.user == request.user:
        context['is_owner'] = True
    else:
        context['is_owner'] = False
    if request.method == 'POST':
        if request.user == company.user:
            opportunity.name = request.POST.get('name')
            opportunity.register_url = request.POST.get('registeration_url')
            company.save()
            opportunity.company = company
            opportunity.description = request.POST.get('description')
            opp_tags = request.POST.getlist('position_name')
            opportunity.save()
            for opp_tag in opp_tags:
                tag = OpportunityTag.objects.get(name=opp_tag)
                opportunity.tags.add(tag)
            return HttpResponseRedirect('/sotm/companies/'+str(company.id))
    print(context)
    return render(request,'sotm/edit_opportunity.html',context)

def internships(request):
    context = {}
    all_positions = OpportunityTag.objects.all()
    context['positions'] = all_positions # all the tags
    verified_companies = Company.objects.filter(verified=True)
    context['companies'] = verified_companies
    all_opportunities = []
    for company in verified_companies:
        for opp in Opportunity.objects.filter(company=company).order_by("create_date"):
            all_opportunities.append(opp)
    context['all_opportunities'] = all_opportunities
    positions_dic = {}
    for position in all_positions:
        opp_list = []
        for opp in all_opportunities:
            if position in opp.tags.all():
                opp_list.append(opp)
        positions_dic[position.name+'_dsc']=opp_list
        opp_list =  list(reversed(opp_list))
        positions_dic[position.name+'_asc']=opp_list

        positions_dic[position.name]=opp_list
    positions_dic['All_dsc'] = all_opportunities
    positions_dic['All_asc'] = list(reversed(all_opportunities))
    context['positions_dic'] = positions_dic
    context['active_position'] = all_positions.first().name+'_asc'
    context['active_pos'] = all_positions.first().name
    return render(request,'sotm/internships.html',context)

def opportunity_view(request,opp_id):
    opportunity = get_object_or_404(Opportunity,id=opp_id)
    context = {}
    context['opportunity'] = opportunity
    student = None
    company = None
    if request.user.is_authenticated :
        student = Student.objects.filter(user=request.user).first()
        company = Company.objects.filter(user=request.user).first()
    if student != None:
        context['is_student'] = True
    else:
        context['is_student'] = False
    if company != None:
        if opportunity.company == company:
            context['is_owner'] = True
        else:
            context['is_owner'] = False
    else:
        context['is_owner'] = False
    return render(request,'sotm/view_opportunity.html',context)

@login_required
def create_new_position(request,company_id):
    company = get_object_or_404(Company,id=company_id)
    context = {}
    positions = OpportunityTag.objects.all()
    context['positions'] = positions
    if company.user == request.user:
        context['is_owner'] = True
    else:
        context['is_owner'] = False
    if request.method == 'POST':
        if request.user == company.user:
            names = []
            for position in positions:
                names.append(position.name)
            name = request.POST.get('position_name')
            if name not in names:
                tag = OpportunityTag()
                tag.name = name
                tag.save()
                return HttpResponseRedirect('/sotm/')
    return render(request,'sotm/sotm_create_position.html',context)

def sotm_register(request):
    if request.method == 'POST':
        if 'student' in request.POST:
            student= Student()
            user = User()
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password1'))
            user.save()
            student.user = user
            student.save()
            return redirect('/sotm/login')
        elif 'company' in request.POST:
            company = Company()
            user = User()
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password1'))
            user.save()
            company.user = user
            company.company_name = request.POST.get('company_name')
            company.vision = request.POST.get('vision')
            company.domain = request.POST.get('domain')
            company.founders = request.POST.get('founders')
            company.company_phone = request.POST.get('company_phone')
            company.founding_year = request.POST.get('founding_year')
            company.facebook = request.POST.get('facebook')
            company.linkedin = request.POST.get('linkedin')
            company.instagram = request.POST.get('instagram')
            company.website = request.POST.get('website')
            company.company_phone = request.POST.get('phone')
            if(request.FILES['company_logo'] is not None):
                company.logo = request.FILES['company_logo']
            company.save()
            company.new_registeration()
            return redirect('/sotm/login')
    context = {}
    return render(request,'sotm/register.html',context)

def sotm_login(request):
    if request.method == 'POST':
        if 'student' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user != None:
                login(request,user)
                return redirect('/sotm/')
        elif 'company' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user != None:
                login(request,user)
                return redirect('/sotm/')
    return render(request,'sotm/login.html')

@login_required
def sotm_logout(request):
    logout(request)
    return redirect('/sotm/')

@login_required
def profile_view(request):
    companies = Company.objects.all()
    for company in companies:
        if request.user == company.user:
            # context = {}
            # if company.user == request.user:
            #     context['is_owner'] = True
            # else:
            #     context['is_owner'] = False
            # context['company'] = company
            # context['opportunities'] = company.get_opportunities()
            # return render(request,'sotm/company_view.html',context)
            return company_view(request,company.id)
    pass