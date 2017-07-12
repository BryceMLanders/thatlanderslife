from django.conf.urls import url
from .views import all_donations

urlpatterns = [
    url(r'^$', all_donations, name='donate'),
]