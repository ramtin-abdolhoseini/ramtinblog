from django.urls import path
from accounts.views import *


app_name='accounts'
#login
#logout
#signup
urlpatterns=[
path('login',login_view,name='login'),
path('logout',logout_view,name='logout'),
path('signup',signup,name='signup'),


]