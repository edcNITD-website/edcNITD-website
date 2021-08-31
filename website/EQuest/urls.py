from django.urls import path
from .views import GenrePostListView,PostListView,PostDetailView
from . import views
# . refers to home directory
# we add variables to url to toggle between posts. pk means primary key
urlpatterns = [ 
    path('', PostListView.as_view(),name='post-list'),
    path('user/<str:username>', GenrePostListView.as_view(),name='genre-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
]