from django.contrib import admin
from website.models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','subject','email','created_date','updated_date']
    search_fields=['name','subject']
    list_filter=['email']
    date_hierarchy='created_date'
admin.site.register(Contact,ContactAdmin)
admin.site.register(newsletter)