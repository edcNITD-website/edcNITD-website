from operator import truediv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from campus_ambassador.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import uuid
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json
# Create your views here.
# utitlity functions

def current_campaign():
    campaigns =  Campaign.objects.filter(start_date__lte=timezone.now(),end_date__gte=timezone.now())
    if campaigns.count() == 0 : 
        result = None
    else:
        result = campaigns[0]
    return result

def generate_amb_code():
    amb_count = Ambassador.objects.all().count()
    new_amb_count = amb_count+1
    str_amb_count = str(new_amb_count)
    if len(str_amb_count)==1:
        str_amb_count = '00'+str_amb_count
    if len(str_amb_count)==2:
        str_amb_count = '0'+str_amb_count
    new_amb_code = 'cap_nitd_'+str_amb_count
    return new_amb_code

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
    context['cur_campaign'] = current_campaign()
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
    new_timeline = []
    for event in timeline:
        new_event = event
        new_event.latest = False
        new_timeline.append(new_event)
    # print(new_timeline)
    for event in new_timeline:
        if not event.completed:
            # print(event)
            event.latest = True
            # print(event.deadline)
            break
    context['incentives'] = incentives
    context['responsibilities'] = responsibilities
    context['timeline'] = new_timeline
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
                # print(get_ambassadors_list())    
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
            # print("hello")
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
            amb.unique_code = generate_amb_code()
            amb.campaign = context['cur_campaign']
            amb.save()
            return redirect('/cap/login')
    return render(request,'campus_ambassador/register.html',context)

@csrf_exempt
def bulk_create(request,secret):
    context = {}
    context = prepareContext(request,context)
    if request.method == 'POST':
        for secret_key in SecretKey.objects.all():
            if secret_key.value == secret:
                user = User()
                json_content = {}
                if 'username' in request.POST:
                    user.username = request.POST['username']
                if 'name' in request.POST:
                    user.first_name=request.POST['name']
                if 'email' in request.POST:
                    user.email = request.POST['email']
                if 'password' in request.POST:
                    user.set_password(request.POST.get('password'))
                try:
                    user.save()
                except IntegrityError:
                    messages.error(request,'Integrity Error, the username exists already, please use another username to register.')
                    json_content= {}
                    json_content['success'] = False
                    # print(json_content)
                    return JsonResponse(data=json_content,safe=False)
                amb = Ambassador()
                amb.user = user
                if 'college' in request.POST:
                    amb.college = request.POST['college']
                if 'phone' in request.POST:
                    amb.phone = request.POST['phone']
                amb.unique_code = generate_amb_code()
                amb.campaign = context['cur_campaign']
                amb.save()
                json_content= {}
                json_content['amb_code'] = amb.unique_code
                json_content['success'] = True
                # print(json_content)
                return JsonResponse(data=json_content,safe=False)
    return HttpResponse("Not found")

@login_required
def edit_profile(request):
    context = {}
    context= prepareContext(request,context)
    if context['is_ambassador']:
        avatars = Avatar.objects.all()
        new_avatars = []
        for avatar in avatars:
            new_avatar = avatar
            new_avatar.selected = avatar.image_url == context['amb'].profile_img
            new_avatars.append(new_avatar)
        context['avatars'] = new_avatars
    if request.method == 'POST':
        if context['is_ambassador']:
            if 'edit_amb' in request.POST:
                amb= context['amb']
                amb.facebook = request.POST.get('facebook')
                amb.linkedin = request.POST.get('linkedin')
                amb.instagram = request.POST.get('instagram')
                if '' != request.POST.get('profile_img') or None != request.POST.get('profile_img'):
                    amb.profile_img = request.POST.get('profile_img')
                if '' != request.POST.get('new_password'):
                    user = amb.user
                    user.set_password(request.POST.get('new_password'))
                    user.save()
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
    elif context['is_moderator']:
        context['user_details'] = CAPModerator.objects.get(user=request.user)
    else:
        context['user_details'] = request.user
    return render(request,'campus_ambassador/profile.html',context)

def forgot_password(request):
    context = {}
    context = prepareContext(request,context)
    return render(request,'campus_ambassador/forgotten_password.html',context)


def task_list(request):
    context={}
    context = prepareContext(request,context)
    all_tasks = Task.objects.filter(campaign=context['cur_campaign'])
    final_all_tasks = []
    for task in all_tasks:
        new_task = task
        new_task.subtasks = SubTask.objects.filter(task=task)
        final_all_tasks.append(new_task)
    tasks_per_page = 2
    if context['is_moderator']:
        tasks_per_page = 5
    paginator_obj = Paginator(final_all_tasks, tasks_per_page)
    page_num = request.GET.get('page_num')
    try:
        pageObj = paginator_obj.get_page(page_num)
    except PageNotAnInteger:
        pageObj = paginator_obj.get_page(1)
    except EmptyPage:
        pageObj = paginator_obj.get_page(paginator_obj.num_pages)
    context['tasks_list'] = pageObj
    context['program_has_ended'] = False
    context['next_campaign_exits'] = False
    if context['is_ambassador']:
        amb = context['amb']
        cur_task = amb.get_current_task
        context['status']={
            'code':201,
            'msg':'Task found',
        }
        if cur_task!=None:
            timeleft = cur_task.end_date - timezone.now()
            context['secs_left'] = timeleft.total_seconds()
            
        if cur_task == None:
            next_task = Task.objects.filter(start_date__gte=timezone.now()).order_by('start_date')
            if next_task.count() == 0:
                # finished all the tasks
                
                # show end of tasks and to standby for announcements of results
                context['status'] = {
                    'code': 202,
                    'msg':'Tasks for the campaign ambassador program have reached a close. Please look out for announcemet of results in your mails soon.',
                }
            else:
                # store next_task__start_date
                # send this via context to user
                next_task = next_task[0]
                context['next_start_date'] = next_task.start_date
                context['status'] = {
                    'code': 204,
                    'msg':'No active task, but task is upcoming on '+str(next_task.start_date.date()),
                }
                timeleft = next_task.start_date - timezone.now()
                context['secs_left'] = timeleft.total_seconds()
                # no task exists for now
    # show next amb program if cur program start date > amb_campaign_end_date
    # show amb program has come to an end for cur_program = none
    if context['cur_campaign'] == None:
        context['program_has_ended'] = True
    if 'amb' in context:
        if context['cur_campaign'].start_date > context['amb'].campaign.end_date:
            context['next_campaign_exits'] = True    
    if context['is_ambassador']:
        context['user_details'] = Ambassador.objects.get(user=request.user)
    elif context['is_moderator']:
        context['user_details'] = CAPModerator.objects.get(user=request.user)
    else:
        context['user_details'] = request.user
    return render(request,'campus_ambassador/task_list.html',context)

@login_required
def score_task(request):
    context = {}
    context = prepareContext(request,context)
    all_cur_ambassadors = Ambassador.objects.filter(campaign=context['cur_campaign']).order_by('unique_code')
    all_subtasks = []
    for task in Task.objects.filter(campaign=context['cur_campaign']).order_by('number'):
        subtasks = SubTask.objects.filter(task=task).order_by('number')
        for st in subtasks:
            all_subtasks.append(st)
    context['subtasks'] = all_subtasks
    amb_per_page = 10
    paginator_obj = Paginator(all_cur_ambassadors, amb_per_page)
    page_num = request.GET.get('page_num')
    try:
        pageObj = paginator_obj.get_page(page_num)
    except PageNotAnInteger:
        pageObj = paginator_obj.get_page(1)
    except EmptyPage:
        pageObj = paginator_obj.get_page(paginator_obj.num_pages)
    context['page_num'] = page_num
    context['ambassadors'] = pageObj
    return render(request,'campus_ambassador/score_task.html',context)

# scoring views
@login_required
def completed_subtask(request,amb_uid):
    context = {}
    context = prepareContext(request,context)
    subtask = '1.1'
    next_url = '/cap/score_task/'
    id = 0
    if 'subtask' in request.GET:
        subtask= request.GET.get('subtask')
    if 'page_num' in request.GET:
        if request.GET.get('page_num')!='':
            next_url+='?page_num='+request.GET.get('page_num')
    if 'id' in request.GET:
        id = request.GET.get('id')
    # completed_subtask = SubtaskCompleted()
    task_num = subtask.split('.')[0]
    subtask_num = subtask.split('.')[1]
    task = Task.objects.get(campaign=context['cur_campaign'],number= task_num)
    subtask = SubTask.objects.filter(task=task,number=subtask_num)
    if(subtask.count()!=0):
        subtask = subtask[0]
    amb = Ambassador.objects.get(id=id)
    amb.subtasks_completed += str(subtask.id)+'|'
    amb.score += subtask.score
    amb.save()
    return redirect(next_url)

@login_required
def remove_comp_subtask(request,amb_uid):
    context = {}
    context = prepareContext(request,context)
    subtask = '1.1'
    next_url = '/cap/score_task/'
    id = 0
    if 'subtask' in request.GET:
        subtask= request.GET.get('subtask')
    if 'page_num' in request.GET:
        if request.GET.get('page_num')!='':
            next_url+='?page_num='+request.GET.get('page_num')
    if 'id' in request.GET:
        id = request.GET.get('id')
    task_num = subtask.split('.')[0]
    subtask_num = subtask.split('.')[1]
    task = Task.objects.get(campaign=context['cur_campaign'],number= task_num)
    subtask = SubTask.objects.filter(task=task,number=subtask_num)
    if(subtask.count()!=0):
        subtask = subtask[0]
    amb = Ambassador.objects.get(id=id)
    # print(subtask.id)
    new_subtask_list = ''
    for st in amb.get_all_subtasks:
        # print(st.id)
        if st.completed:
            if st.id ==subtask.id:
                amb.score -= subtask.score
                continue
            else:
                new_subtask_list+=str(st.id)+'|'
    amb.subtasks_completed = new_subtask_list
    # print(new_subtask_list)
    amb.save()
    return redirect(next_url)

def all_ambassadors(request):
    context = {}
    return render(request,'campus_ambassador/home.html',context)

# Ambasssador and Moderator views
def leaderboard(request):
    context = {}
    context = prepareContext(request,context)
    ambassadors = Ambassador.objects.filter(campaign=context['cur_campaign']).order_by('-score')
    current_rank = 0
    
    for ambassador in ambassadors:
            current_rank += 1
            ambassador.rank = current_rank
    context['ambassadors'] = ambassadors
    context['current_rank'] = current_rank
    return render(request,'campus_ambassador/leaderboard.html',context)

