from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from esummit.models import Year_Detail
from django.core.paginator import Paginator
from django.db.models import Count
def home_page(request):
    context={
        'posts': Post.objects.all(),
    }
    return render(request,'EQuest/post_list.html',context)


def post_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()  # <appname>/<model>_<viewtype>.html
    post=Post.objects.all()
    count = post.count()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        post=post.filter(category = category)
    categories = Category.objects.all().annotate(posts_count=Count('post'))
    
    year = Year_Detail.objects.all().order_by("-year")
    max_year=0
    max_id=0
    for y in Year_Detail.objects.all():
        if(y.year>max_year):
            max_year=y.year
            max_id=y.id
    return render(request,'EQuest/post_list.html',{'categories':categories,
                                                   'category':category,
                                                   'post': post,
                                                   'count':count,
                                                   'years' :year,
                                                   'latest' :max_id, 
                                                   'latest_year' :max_year%100,
                                                 })

def post_detail(request,id):
    post=get_object_or_404(Post,id=id) 
    category=None
    categories=Category.objects.all()

    count = Post.objects.all().count()
    categories = Category.objects.all().annotate(posts_count=Count('post'))
    return render(request,'EQuest/post_detail.html',{'post':post,
                                                    'categories':categories,
                                                    'count':count,
                                                    })
                                                

