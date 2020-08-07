from django.contrib import admin
from .models import UpcomingEvent,OtherEvent

event_models=[UpcomingEvent,OtherEvent]
admin.site.register(event_models)