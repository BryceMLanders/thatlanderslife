from django.conf.urls import url
from photos.views import *
from .views import *
 
urlpatterns = [
    url(r'^$', photos_by_tags, name='photos'),
    url(r'^$', photos_by_ireland, name='ireland'),
    url(r'^$', photos_by_girls, name='girls'),
    url(r'^$', photos_by_van, name='van'),
    url(r'^$', photos_by_friends, name='friends'),
    
]