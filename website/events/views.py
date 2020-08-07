from django.shortcuts import render
from .models import UpcomingEvent,OtherEvent

def event(request):
    context={
        'upcomingevent' : UpcomingEvent.objects.all(),
        'otherevent' : OtherEvent.objects.all()
    }
    return render(request, 'events/event_page.html', context)
