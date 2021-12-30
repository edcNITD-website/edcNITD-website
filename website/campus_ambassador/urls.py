from django.urls import path
from campus_ambassador.views import *

app_name = "cap"

urlpatterns = [
 path("",home,name="cap_home_page"),
]
