"""Authenticate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path("", views.start_page, name = "start_page"),
    path("workingpage", views.working_page, name = "working_page"),
    path("index", views.index, name = "index"),
    path("profile", views.profile, name="profile"),
    path("register",views.register,name = "register"),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url("buttons", views.buttons, name='buttons'),
    url("video", views.video, name='buttons'),
    url(r'^post/(?P<pk>\d+)/remove_post/$', views.remove_post, name='remove_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^profile/new/$', views.profle_new, name='profile_new'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name='profile_detail'),

]
