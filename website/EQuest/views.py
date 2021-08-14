from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView # to see details of every post
from .models import Post

def home_page(request):
    context={
        'posts': Post.objects.all(),
    }
    return render(request,'EQuest/post_list.html',context)
class PostListView(ListView):
    model=Post
    template_name="EQuest/post_list.html"  # <appname>/<model>_<viewtype>.html
    context_object_name= 'posts'# to help recognize name of variable as posts
    ordering=['-date'] # to ensure newest posts come on top. Remove minus sign for reverse.
    paginate_by=5
class GenrePostListView(ListView):
    model=Post
    template_name="blog/genre_posts.html"  # <appname>/<model>_<viewtype>.html
    context_object_name= 'posts'# to help recognize name of variable as posts
    ordering=['-date'] # to ensure newest posts come on top. Remove minus sign for reverse.
    paginate_by=5

    def get_queryset(self):
        genre_check=get_object_or_404(Post,genre_check=self.kwargs.get('genre'))
        return Post.objects.filter(genre=genre_check).order_by('-date')
class PostDetailView(DetailView):
     model=Post
     template_name="EQuest/post_detail.html"
     #return render(request,'EQuest/post_list.html',context)
