from django.urls import path
from . import views

urlpatterns = [
 path("",views.web_team,name="web_team"),
]
