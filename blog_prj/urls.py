"""blog_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import post_list
from django.views.static import serve
from accounts import urls as accounts_urls
# from home import urls as home_urls
from home.views import home

from blog import urls as blog_urls
from photos import urls as photos_urls
from contact import urls as contact_urls
from donate import urls as donate_urls
from payments import urls as payment_urls
from bio import urls as bio_urls
from django.conf import settings

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$',home , name='index'),
    url(r'^blog/', include(blog_urls)),
    url(r'^user/',include(accounts_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^user/', include(accounts_urls)),
    url(r'^photos/', include(photos_urls)),
    url(r'^contact/', include(contact_urls)),
    url(r'^donate/', include(donate_urls)),
    url(r'^payments/', include(payment_urls)),
    url(r'^bio/', include(bio_urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns