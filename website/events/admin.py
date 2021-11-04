from django.contrib import admin
from .models import*

event_models=[Event]
admin.site.register(event_models)

event_images=[EventImages]
admin.site.register(event_images)

timeline_details=[Timeline]
admin.site.register(timeline_details)