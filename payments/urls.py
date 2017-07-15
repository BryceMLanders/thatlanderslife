from django.conf.urls import url
from .views import donate_now

urlpatterns = [
    url(r'^donate_now/(?P<id>\d+)', donate_now, name='donate_now_stripe'),
]