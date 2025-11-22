from django.contrib import admin
from blog.models import Post,Category,comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
# field - exclude-list display
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy ='created_date'
    empty_value_display='-empty-'
    list_display=["title","author",'login_required',"counted_view","status","published_date",'created_date']
    summernote_fields = ('content',)
    ordering=['created_date']
    list_filter=['status','author','login_required']
    search_fields=["title","content"]



class CommentAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    ordering=['-created_date']
    list_display=['name','subject','email','post','approaved','created_date']
    search_fields=['message','post']
    list_filter=['approaved','name','post']
    empty_value_display='-empty-'



admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(comment,CommentAdmin)