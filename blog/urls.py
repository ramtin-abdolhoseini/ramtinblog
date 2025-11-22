from django.urls import path
from blog.views import *

app_name="blog"

urlpatterns = [
    path('',blog_home,name='blog-home'),
    path('<int:pid>',blog_single,name='blog-single'),
    path('category/<str:cat_name>',blog_home,name='category'),
    path('author/<str:author_name>',blog_home,name='author'),
    path('search/',blog_search,name='search'), 
    path('tag/<str:name>',tag,name='tag'),

 
   
]