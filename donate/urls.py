from django.conf.urls import url
from donate.views import *
from .views import donate
 
urlpatterns = [
    url(r'^$', donate, name='donate'),
    
]