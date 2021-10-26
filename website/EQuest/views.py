from django.shortcuts import render, get_object_or_404
from .models import Category, Post

def home_page(request):
    context={
        'posts': Post.objects.all(),
    }
    return render(request,'EQuest/post_list.html',context)


def post_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()  # <appname>/<model>_<viewtype>.html
    post=Post.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        post=post.filter(category = category)
    return render(request,'EQuest/post_list.html',{'categories':categories,
                                                   'category':category,
                                                   'post': post,
                                                  })
def post_detail(request,id):
    post=get_object_or_404(Post,id=id) 
    category=None
    categories=Category.objects.all()
    count=Post.objects.all().count()
    return render(request,'EQuest/post_detail.html',{'post':post,
                                                    'categories':categories,
                                                    })