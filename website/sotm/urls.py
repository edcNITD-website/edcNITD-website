from django.urls import path
from . import views

app_name = 'sotm'

urlpatterns = [
    path("",views.sotm_home,name="sotm_home"),
    path('companies/<int:company_id>/create_position/',views.create_new_position,name='create_position'),
    path("companies/profile/",views.profile_view,name='profile_view'),
    path("student/profile/",views.profile_view,name='profile_view'),
    path('companies/<int:company_id>/opportunity/edit/<int:opp_id>',views.edit_opportunity,name='edit_opportunity'),
    path('companies/<int:company_id>/opportunity/delete/<int:opp_id>',views.delete_opportunity,name='delete_opportunity'),
    path('opportunity/<int:opp_id>',views.opportunity_view,name='view_opportunity'),
    path('companies/<int:company_id>/add_position/',views.sotm_add_opportunity,name='add_position'),
    path('companies/<int:company_id>/remove_position/',views.sotm_remove_opportunity,name='remove_position'),
    path('internships/',views.internships,name='internships'),
    path("companies/",views.sotm_companies,name='companies'),
    path("companies/<int:company_id>",views.company_view,name='company_view'),
    path("student/<int:student_id>",views.student_view,name='student_view'),
    path("companies/edit/<int:company_id>",views.company_edit,name='company_edit'),
    path("student/edit/<int:student_id>",views.student_edit,name='student_edit'),
    path('register/',views.sotm_register,name='register'),
    path('login/',views.sotm_login,name='login'),
    path('logout/',views.sotm_logout,name='logout'),
    path('forgotten_password/',views.forgotten_password,name='forgotten_password'),
    path('key/<str:key_value>/',views.key,name='key_view'),
    path('change_password/',views.change_password,name='change_password'),
]
