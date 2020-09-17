from django.shortcuts import render
from .models import Members

# Create your views here.

def web_team(request):
    return render(request,'web_team/web_team.html')
