from django.contrib import admin

# Register your models here.
from campus_ambassador.models import *
admin.site.register(Incentive)
admin.site.register(Responsibliity)
admin.site.register(TimeLineEvent)
admin.site.register(FAQ)
admin.site.register(Ambassador)
admin.site.register(CAPModerator)