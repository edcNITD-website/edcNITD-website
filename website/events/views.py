from django.shortcuts import render

def event(requests):
    return render(requests,'events/event_page.html')