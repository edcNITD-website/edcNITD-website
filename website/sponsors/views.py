from django.shortcuts import render, HttpResponse
from sponsors.models import *


# Create your views here.
def sponsors(request):
    esummit = Esummit.objects.all().order_by('-year')
    events = Event.objects.all()
    sponsors = Sponsor.objects.all()
    # new_sponsors = []
    for sponsor in sponsors:
        print(sponsor,sponsor.event_set.all())
    #     new_sponsor = {}
    #     new_sponsor['events'] = Event.objects.all().filter(event_sponsors_set=sponsor)
    return render(request, 'sponsors/sponsors.html', {'esummit': esummit, 'events': events, 'sponsors': sponsors})
