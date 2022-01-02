from django.urls import path
from campus_ambassador.views import *

app_name = "cap"

urlpatterns = [
    path("",home,name="cap_home_page"),
    path("login/",cap_login,name='login'),
    path("register/",register,name='register'),
    path("logout/",cap_logout,name="logout"),
    path("profile/",profile,name='profile'),
]
