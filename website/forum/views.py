from django.shortcuts import render

def Home(request):
    return render(request,'forum/home_page.html');