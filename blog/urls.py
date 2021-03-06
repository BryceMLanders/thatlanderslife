from django.conf.urls import url
from blog.views import *
 
urlpatterns = [
    url(r'^$', post_list, name='blog'),
    url(r'^(?P<id>\d+)/$', post_detail, name='view_post'),
    url(r'^post/new/$', new_post, name='new_post'),
    url(r'(?P<id>\d+)/edit$', edit_post, name='edit'),
    url(r'^tag/$', tag_list, name='tag')

]