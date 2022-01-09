from django.shortcuts import render
from campus_ambassador.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import uuid
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import math
# Create your views here.
# utitlity functions
def calc_precedence(index):
    precedence = 0
    precedence = int(index.split('-')[0])*1000+int(index.split('-')[1])
    return precedence

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

def prepareContext(request,context)->dict :
    user = request.user
    context['is_staff'] = request.user.is_staff
    context['is_ambassador'] = user in get_ambassadors_list()
    context['is_moderator'] = user in get_moderators_list()
    if context['is_ambassador']:
        context['amb'] = Ambassador.objects.get(user=request.user)
    elif context['is_moderator']:
        context['mod'] = CAPModerator.objects.get(user=request.user)
    return context
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
                if user.is_staff:
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
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
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
            amb.unique_code = uuid.uuid4().hex[:8]
            print(amb)
            amb.save()
            return redirect('/cap/login')
    return render(request,'campus_ambassador/register.html',context)

@login_required
def edit_profile(request):
    context = {}
    context= prepareContext(request,context)
    if request.method == 'POST':
        if context['is_ambassador']:
            if 'edit_amb' in request.POST:
                amb= context['amb']
                user = amb.user
                user.first_name = request.POST.get('firstname')
                user.last_name = request.POST.get('lastname')
                user.save()
                amb.college = request.POST.get('college')
                amb.phone = request.POST.get('phone')
                amb.facebook = request.POST.get('facebook')
                amb.linkedin = request.POST.get('linkedin')
                amb.instagram = request.POST.get('instagram')
                amb.save()
                return redirect('/cap/profile')
        if context['is_moderator']:
            if 'edit_mod' in request.POST:
                mod= context['mod']
                user = mod.user
                user.first_name = request.POST.get('firstname')
                user.last_name = request.POST.get('lastname')
                user.save()
                mod.phone = request.POST.get('phone')
                mod.save()
                return redirect('/cap/profile')
    return render(request,'campus_ambassador/edit_profile.html',context)

@login_required
def cap_logout(request):
    context = {}
    logout(request)
    return render(request,'campus_ambassador/home.html',context)

# Ambassador views
@login_required
def profile(request):
    context = {}
    context = prepareContext(request,context)
    if context['is_ambassador']:
        context['user_details'] = Ambassador.objects.get(user=request.user)
        context['pending_stcr'] = SubTaskCompletionRequest.objects.filter(ambassador=context['amb'],completed=False).order_by('-creation_date')
        context['completed_stcr'] = SubTaskCompletionRequest.objects.filter(ambassador=context['amb'],completed=True).order_by('-creation_date')
    elif context['is_moderator']:
        context['user_details'] = CAPModerator.objects.get(user=request.user)
    else:
        context['user_details'] = request.user
    return render(request,'campus_ambassador/profile.html',context)

@login_required
def create_request(request,subtask_id):
    context = {}
    context = prepareContext(request,context)
    subtask = get_object_or_404(SubTask,id=subtask_id)
    all_stcr = SubTaskCompletionRequest.objects.all()
    for stcr in all_stcr:
        if stcr.ambassador == context['amb']:
            if stcr.subtask == subtask:
                return redirect('/cap/profile')
    if context['is_ambassador']:
        stcr_request = SubTaskCompletionRequest()
        stcr_request.ambassador = context['amb']
        stcr_request.subtask = subtask
        stcr_request.unique_id = uuid.uuid4().hex[:8]
        stcr_request.save()
        print("Request created with id "+stcr_request.unique_id)
    return redirect('/cap/profile')

# Moderator views
def all_tasks(request):
    context = {}
    context = prepareContext(request,context)
    tasks = None
    if context['is_moderator'] or context['is_staff']:
        tasks = Task.objects.all().order_by('number')
    context['tasks'] = tasks
    return render(request,'campus_ambassador/all_tasks.html',context)

def has_higher_precedence_subtask(current_task):
    current_precedence = calc_precedence(current_task)
    result = {}
    subtasks = SubTask.objects.all()
    result['exists'] = False
    for subtask in subtasks:
        if subtask.precedence > current_precedence:
            result['exists'] = True
            result['next_subtask'] = subtask.index
    
    return result

@login_required
def manage_stcr(request,stcr_id):
    context = {}
    context = prepareContext(request,context)
    if context['is_moderator']:
        stcr = get_object_or_404(SubTaskCompletionRequest,id=stcr_id)
        context['stcr_request'] = stcr
        if request.method=='POST':
            if 'delete' in request.POST:
                stcr.ambassador.score -= stcr.score_allotted
                stcr.ambassador.save()
                stcr.delete()
                return redirect('/cap/profile')
            if 'save_stcr' in request.POST:
                if int(request.POST.get('score'))  <= stcr.subtask.score:
                    if calc_precedence(stcr.ambassador.current_task) > stcr.subtask.precedence :
                        stcr.ambassador.score += int(request.POST.get('score'))-stcr.score_allotted
                        stcr.ambassador.save()
                        stcr.score_allotted = request.POST.get('score')
                    else:
                        stcr.ambassador.score += int(request.POST.get('score'))-stcr.score_allotted
                        if has_higher_precedence_subtask(stcr.ambassador.current_task)['exists']:
                            stcr.ambassador.current_task = has_higher_precedence_subtask(stcr.ambassador.current_task)['next_subtask']
                        stcr.ambassador.save()
                        stcr.score_allotted = request.POST.get('score')
                    stcr.score_allotted = request.POST.get('score')
                    stcr.completed = request.POST.get('completed')=='on'
                    stcr.save()
            return redirect('/cap/profile')
    else:
        return redirect('/cap/profile')
    return render(request,'campus_ambassador/manage_stcr.html',context)

@login_required
def pending_stcr(request):
    context = {}
    context = prepareContext(request,context)
    if context['is_moderator']:
        all_pending = SubTaskCompletionRequest.objects.filter(completed=False).order_by('-creation_date')
        task_per_page = 5
        paginatorObject = Paginator(all_pending, task_per_page)
        context['last_page'] = math.ceil(all_pending.count()/task_per_page)
        context['before_last_page'] = math.ceil(all_pending.count()/task_per_page)-1
        pageNumber = request.GET.get('page')
        try:
            pageObj = paginatorObject.get_page(pageNumber)
        except PageNotAnInteger:
            pageObj = paginatorObject.get_page(1)
        except EmptyPage:
            pageObj = paginatorObject.get_page(paginatorObject.num_pages)
        context['requests']=pageObj
    else:
        return redirect('/cap/profile')
    print(pageObj.number)
    return render(request,'campus_ambassador/pending.html',context)

@login_required
def completed_stcr(request):
    context = {}
    context = prepareContext(request,context)
    if context['is_moderator']:
        all_completed = SubTaskCompletionRequest.objects.filter(completed=True).order_by('-creation_date')
        task_per_page = 5
        paginatorObject = Paginator(all_completed, task_per_page)
        context['last_page'] = math.ceil(all_completed.count()/task_per_page)
        context['before_last_page'] = math.ceil(all_completed.count()/task_per_page)-1
        pageNumber = request.GET.get('page')
        try:
            pageObj = paginatorObject.get_page(pageNumber)
        except PageNotAnInteger:
            pageObj = paginatorObject.get_page(1)
        except EmptyPage:
            pageObj = paginatorObject.get_page(paginatorObject.num_pages)
        context['requests']=pageObj
    else:
        return redirect('/cap/profile')
    return render(request,'campus_ambassador/completed_tasks.html',context)
def all_ambassadors(request):
    context = {}
    return render(request,'campus_ambassador/home.html',context)

# Ambasssador and Moderator views
def leaderboard(request):
    context = {}
    return render(request,'campus_ambassador/home.html',context)