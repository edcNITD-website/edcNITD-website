from django.shortcuts import render
from campus_ambassador.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db import IntegrityError

# Create your views here.
# utitlity functions 
def prepareContext(request,context)->dict :
    user = request.user
    context['is_staff'] = request.user.is_staff
    context['is_ambassador'] = False
    context['is_moderator'] = False
    return context

def get_ambassadors_list()->list:
    ambassador_list = []
    for amb in Ambassador.objects.all():
        ambassador_list.append(amb.user)
    return ambassador_list

def get_moderators_list()->list:
    moderator_list = []
    for mod in CAPModerator.objects.all():
        moderator_list.append(mod.user)
    return moderator_list
# anonymous user views

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

def cap_login(request):
    context = {}
    context = prepareContext(request,context)
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                messages.success(request,"Successfully logged in.")
                print(get_ambassadors_list())    
                if user in get_ambassadors_list():
                    return redirect('/cap/profile')
                if user in get_moderators_list():
                    return redirect('/cap/profile')
    return render(request,'campus_ambassador/login.html',context)

def register(request):
    context = {}
    context = prepareContext(request,context)
    if request.method == 'POST':
        if 'register' in request.POST:
            print("hello")
            user = User()
            user.username = request.POST.get('username')
            user.set_password(request.POST.get('password'))
            user.email = request.POST.get('email')
            try:
                user.save()
            except IntegrityError:
                messages.error(request,'Integrity Error, the username exists already, please use another username to register.')
                return redirect('/cap/register')
            amb = Ambassador()
            amb.user = user
            amb.college = request.POST.get('college')
            amb.phone = request.POST.get('phone')
            amb.facebook = request.POST.get('facebook')
            amb.linkedin = request.POST.get('linkedin')
            amb.instagram = request.POST.get('instagram')
            print(amb)
            amb.save()
            return redirect('/cap/login')
    return render(request,'campus_ambassador/register.html',context)

def cap_logout(request):
    context = {}
    logout(request)
    return render(request,'campus_ambassador/home.html',context)

# Ambassador views
def profile(request):
    context = {}
    return render(request,'campus_ambassador/profile.html',context)

# Moderator views
def all_tasks(request):
    context = {}
    return render(request,'campus_ambassador/home.html',context)

def all_ambassadors(request):
    context = {}
    return render(request,'campus_ambassador/home.html',context)

# Ambasssador and Moderator views
def leaderboard(request):
    context = {}
    return render(request,'campus_ambassador/home.html',context)