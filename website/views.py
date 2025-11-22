from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from blog.models import Post
from website.models import Contact
from website.forms import FORM_NAME,ContactForm,NewsletterForm
# Create your views here.
def home(request):
    return render(request,"website/index.html")

def about(request):
    return render(request,"website/about.html")

def contact(request):
    
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket doesnt submit')

    form=ContactForm()

    context={'form':form}    
    return render(request,"website/contact.html",context)



def test(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')  
        else:
            HttpResponse('not valid')      
    form=ContactForm()    
    context={'form':form}
    return render(request,'website/test.html',context)



def newsletter(request):
    if request.method=='POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')
  





