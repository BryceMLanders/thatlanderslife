from django.conf.urls import url
from .views import all_donations, make_donation, show_wanted_donations


urlpatterns = [
    url(r'^$', all_donations, name='donate'),
    url(r'^wanted', show_wanted_donations, name='wanted_donation'),
    url(r'^make_donation/(?P<amount>\d+)',make_donation,name= 'make_donation'),]
