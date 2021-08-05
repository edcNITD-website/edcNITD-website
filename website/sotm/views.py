from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from sotm.models import *
from django.contrib.auth.models import User
# Create your views here.
def sotm_home(request):
    context = {}
    context['hero_faqs'] = FAQ.objects.filter(is_hero=True)
    context['normal_faqs'] = FAQ.objects.filter(is_hero=False)
    return render(request,'sotm/sotm_home.html',context)

def sotm_companies(request):
    context = {}
    context['company_list'] = Company.objects.filter(verified=True)
    context['owned_company'] = None
    for company in Company.objects.filter(verified=True):
        if company.user == request.user:
            context['owned_company'] = company        
    return render(request,'sotm/sotm_companies.html',context)

def company_view(request,company_id):
    company = get_object_or_404(Company,id=company_id)
    context = {}
    context['company'] = company
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
        company.save()
        return redirect('/sotm/')
    return render(request,'sotm/company_edit.html',context)

def sotm_register(request):
    if request.method == 'POST':
        if 'student' in request.POST:
            print("student")
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
            company.founding_year = request.POST.get('founding_year')
            company.save()
            return redirect('/sotm/login')
    context = {}
    return render(request,'sotm/register.html',context)

def sotm_login(request):
    if request.method == 'POST':
        if 'student' in request.POST:
            print("student")
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
    if request.method == 'POST':
        user = request.user
        logout(request)
        return redirect('/sotm/')
    return render(request,'sotm/logout.html')