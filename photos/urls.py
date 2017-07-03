from django.conf.urls import url
from photos.views import *
from .views import photos
 
urlpatterns = [
    url(r'^$', photos, name='photos'),
    
]