from django.urls import path
from . import views
# . refers to home directory
# we add variables to url to toggle between posts. pk means primary key
app_name = "EQuest"
urlpatterns = [ 
    path('', views.post_list,name='post_list'),
    path('<slug:category_slug>', views.post_list,name='post_by_category'),
    path('<int:id>/', views.post_detail,name='post_detail'),
]