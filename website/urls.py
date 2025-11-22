from django.urls import path
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from website.views import *

app_name="website"
sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("",home,name='home'),
    path("about",about,name='about'),
    path("contact",contact,name='contact'),
    path('newsletter',newsletter,name='newsletter'),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),
    
]