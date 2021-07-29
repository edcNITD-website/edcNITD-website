from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def sotm_home(request):
    return render(request,'sotm/sotm_home.html')