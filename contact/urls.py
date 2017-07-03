from django.conf.urls import url
from contact.views import *
from .views import contact
 
urlpatterns = [
    url(r'^$', contact, name='contact'),
    
]