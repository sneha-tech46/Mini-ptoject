"""evoting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from user import views as user_views
from evoting import views as admins_views
from party import views as party_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admins_views.index, name='index'),
    path('home/', admins_views.index, name='home'),

    path('userloginpage/', admins_views.userloginpage, name='userloginpage'),
    path('userregister/', admins_views.userregister, name='userregister'),
    path('userregisteraction/', admins_views.userregisteraction, name='userregisteraction'),
    path('AdminActiveUsers/', admins_views.AdminActiveUsers, name='AdminActiveUsers'),
    path('AdminActiveparty/', admins_views.AdminActiveparty, name='AdminActiveparty'),
    
    path('voterloginpage/', admins_views.voterloginpage, name='voterloginpage'),
    path('adminloginpage/', admins_views.adminloginpage, name='adminloginpage'),
    path('adminloginaction/', admins_views.adminloginaction, name='adminloginaction'),
    path('adminlogout/', admins_views.adminlogout, name='adminlogout'),
    path('adminviewvotes/', admins_views.adminviewvotes, name='adminviewvotes'),

    path('adminuserdetails/', admins_views.adminuserdetails, name='adminuserdetails'),
    path('adminvoterdetails/', admins_views.adminvoterdetails, name='adminvoterdetails'),

    path('partyregister/', party_views.partyregister, name='partyregister'),
    path('partyregisteration/', party_views.partyregisteration, name='partyregisteration'),

    path('userloginaction/', user_views.userloginaction, name='userloginaction'),
    path('partyloginaction/', party_views.partyloginaction, name='partyloginaction'),

    path('userfacedetect/', user_views.userfacedetect, name='userfacedetect'),
    path('facedetect/', user_views.facedetect, name='facedetect'),
    path('uservoteridaction/', user_views.uservoteridaction, name='uservoteridaction'),
    path('userotpaction/', user_views.userotpaction, name='userotpaction'),

    path('userlogout/', user_views.userlogout, name='userlogout'),
    path('userpartiesselection/', user_views.userpartiesselection, name='userpartiesselection'),
    path('userprofile/', user_views.userprofile, name='userprofile'),

    path('uservoteparty/', user_views.uservoteparty, name='uservoteparty'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)