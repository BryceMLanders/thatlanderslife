from django.conf.urls import url
from blog.views import *
from .views import post_list
 
urlpatterns = [
    url(r'^$', post_list, name='blog'),
    url(r'^(?P<id>\d+)/$', post_detail, name='view_post'),
    url(r'^post/new/$', new_post, name='new_post'),
    url(r'(?P<id>\d+)/edit$', edit_post, name='edit'),

]