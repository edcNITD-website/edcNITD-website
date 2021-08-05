from django.urls import path
from . import views

app_name = 'sotm'

urlpatterns = [
    path("",views.sotm_home,name="sotm_home"),
    path("companies/",views.sotm_companies,name="companies"),
    path("companies/<int:company_id>",views.company_view,name='company_view'),
    path("companies/edit/<int:company_id>",views.company_edit,name='company_edit'),
    path('register/',views.sotm_register,name='register'),
    path('login/',views.sotm_login,name='login'),
    path('logout/',views.sotm_logout,name='logout'),
]
