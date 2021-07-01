from django.shortcuts import render
from .models import Contributors

# Create your views here.

def web_team(request):
    context={
        'contributors':Contributors.objects.all()
    }
    ordering=['date']
    return render(request,'web_team/web_team.html',context)
