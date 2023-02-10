from django.contrib import admin

# Register your models here.
from sponsors.models import Sponsor, Event, Esummit, EsummitSponsor, Brochure

admin.site.register(Sponsor)
admin.site.register(Event)
admin.site.register(Esummit)
admin.site.register(EsummitSponsor)
admin.site.register(Brochure)
