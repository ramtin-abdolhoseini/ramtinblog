from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from django.core.paginator import Paginator
from blog.models import *
from blog.form import CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def blog_home(request,cat_name=None,author_name=None):
    posts=Post.objects.filter(status=1)
    if author_name!=None:
        posts=posts.filter(author__username=author_name)

    if cat_name!=None:
        posts=posts.filter(category__name=cat_name)

    posts=Paginator(posts,3)
    page_number=request.GET.get('page')
    posts=posts.get_page(page_number)
    context={'posts':posts,'cat_name':cat_name,'author':author_name}
    return render(request,'blog/blog-home.html',context)



def blog_search(request):
    posts=Post.objects.filter(status=1)
    #print(request.__dict__)
    if request.method=='GET':
        #print(request.GET.get('s'))
        posts=posts.filter(content__contains=request.GET.get('s'))
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)


    
#@login_required(login_url='/accounts/login')
def blog_single(request,pid):
    posts=Post.objects.filter(status=1)
    post=get_object_or_404(posts,id=pid)
    if post.login_required==False:
        if request.method=='POST':
            form=CommentForm(request.POST)
            if form.is_valid():
                form.save()
                print(request.POST)
                
                return redirect(request.path)
            
        comments=comment.objects.filter(approaved=True)
        comments=comments.filter(post=post.id).order_by('created_date')
        context={'pid':pid,'post':post,'comments':comments}
        return render(request,'blog/blog-single.html',context)
    else:
        return redirect('/accounts/login')






def tag(request,name):
    posts=Post.objects.filter(status=1)

    posts=posts.filter(tags__name=name)
    context={'posts':posts}
    
    return render(request,'blog/blog-home.html',context)

