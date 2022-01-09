from django.urls import path
from campus_ambassador.views import *

app_name = "cap"

urlpatterns = [
    path("",home,name="cap_home_page"),
    path("login/",cap_login,name='login'),
    path("register/",register,name='register'),
    path("logout/",cap_logout,name="logout"),
    path("profile/",profile,name='profile'),
    path("profile/edit",edit_profile,name='edit_profile'),
    path("create_stcr_request/<int:subtask_id>",create_request,name='create_stcr_request'),
    path("pending/",pending_stcr,name='pending_stcr'),
    path("manage_stcr/<int:stcr_id>",manage_stcr,name='manage_stcr'),
    path("completed/",completed_stcr,name='completed_stcr'),
]
