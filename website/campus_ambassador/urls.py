from django.urls import path
from campus_ambassador.views import *

urlpatterns = [
 path("",home,name="cap_home_page"),
]
