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

# Всевозможные корректные переходы на страницы
urlpatterns = [
    path("", views.start_page, name = "start_page"),
    path("task_page", views.task_page, name = "task_page"),
    path("workingpage", views.working_page, name = "working_page"),
    path("page1", views.page_1, name = "page_1"),
    path("page2", views.page_2, name = "page_2"),
    path("page3", views.page_3, name = "page_3"),
    path("profile", views.profile, name="profile"),
    path("register",views.register,name = "register"),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^comment/(?P<pk>\d+)/new/$', views.comment_new, name='comment_new'),
    url(r'^task/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    url(r'^task/new/$', views.task_new, name='task_new'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url("buttons", views.buttons, name='buttons'),
    url("video", views.video, name='buttons'),
    url(r'^post/(?P<pk>\d+)/remove_post/$', views.remove_post, name='remove_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^task/(?P<pk>\d+)/remove_task/$', views.remove_task, name='remove_task'),
    url(r'^task/(?P<pk>\d+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^post/(?P<pk>\d+)/rating0/$', views.rating_enter0, name='rating_enter0'),
    url(r'^post/(?P<pk>\d+)/rating1/$', views.rating_enter1, name='rating_enter1'),
    url(r'^post/(?P<pk>\d+)/rating2/$', views.rating_enter2, name='rating_enter2'),
    url(r'^post/(?P<pk>\d+)/rating3/$', views.rating_enter3, name='rating_enter3'),
    url(r'^post/(?P<pk>\d+)/rating4/$', views.rating_enter4, name='rating_enter4'),
    url(r'^post/(?P<pk>\d+)/rating5/$', views.rating_enter5, name='rating_enter5'),
    url(r'^post/(?P<pk>\d+)/rating6/$', views.rating_enter6, name='rating_enter6'),
    url(r'^post/(?P<pk>\d+)/rating7/$', views.rating_enter7, name='rating_enter7'),
    url(r'^post/(?P<pk>\d+)/rating8/$', views.rating_enter8, name='rating_enter8'),
    url(r'^post/(?P<pk>\d+)/rating9/$', views.rating_enter9, name='rating_enter9'),
    url(r'^post/(?P<pk>\d+)/rating10/$', views.rating_enter10, name='rating_enter10'),
    url(r'^profile/new/$', views.profle_new, name='profile_new'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name='profile_detail'),

]
