from django.db import models
from django.contrib.auth.models  import User
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField()
    def __str__(self):
        return self.name 
    

class Post(models.Model):
    title=models.CharField()
    content=models.TextField()
    login_required=models.BooleanField(default=False)
    image=models.ImageField(upload_to='blog',default='blog/default.jpg')
    tags = TaggableManager()
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    counted_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    updated_date=models.DateTimeField(auto_now=True,null=True)
    published_date=models.DateTimeField(null=True)
    class Meta:
        ordering=["created_date"]
        #verbose_name='پست'
        #verbose_name_plural='پست ها'
    def __str__(self):
        return f"{self.id}- {self.title}"
    
    #def snippets(self):
        #return self.content[:100]+'...'

    def get_absolute_url(self):
        return reverse('blog:blog-single',kwargs={'pid':self.id})
    

class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    name=models.CharField()
    subject=models.CharField()
    email=models.EmailField()
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    uploaded_date=models.DateTimeField(auto_now=True)
    approaved=models.BooleanField(default=False)

    class Meta():
        ordering=['-created_date']

    def __str__(self):
        return self.name