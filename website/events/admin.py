from django.contrib import admin
from .models import*

event_models=[Event]
admin.site.register(event_models)