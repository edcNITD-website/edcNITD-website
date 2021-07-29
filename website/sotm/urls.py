from django.urls import path
from . import views

urlpatterns = [
    path("",views.sotm_home,name="sotm_home"),
]
