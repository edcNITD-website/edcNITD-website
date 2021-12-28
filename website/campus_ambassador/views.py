from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request,'campus_ambassador/home.html',context)