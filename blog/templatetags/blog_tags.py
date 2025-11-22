from django import template
from blog.models import *
from django.shortcuts import render,get_object_or_404
register=template.Library()


@register.simple_tag
def hello():
    return 'hello'


@register.simple_tag(name='posts')
def f():
    posts=Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg):
    return value[:arg]

@register.inclusion_tag('blog/blog-popular-post.html')
def popularposts(arg=4):
    posts=Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}


@register.inclusion_tag('blog/post-category.html')
def all_category():
    posts=Post.objects.filter(status=1)
    categorys=Category.objects.all()
    cat_name={}
    for name in categorys:
        cat_name[name]=posts.filter(category=name).count() #catname={name:int}
    return {'categorys':cat_name}

@register.simple_tag(name='comments_count')
def comments(pid):
    post=Post.objects.get(pk=pid)
    comments=comment.objects.filter(approaved=True)
    return comments.filter(post=post.id).count()
   