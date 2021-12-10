from django.contrib import admin
from .models import Post,Category,PostImage
# Register your models here.
admin.site.register(Category)
class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Post
 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass