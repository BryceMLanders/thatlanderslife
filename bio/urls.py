from django.conf.urls import url
from bio.views import *
from .views import bio
 
urlpatterns = [
    url(r'^$', bio, name='bio'),
    
]