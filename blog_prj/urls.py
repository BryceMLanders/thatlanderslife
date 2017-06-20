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
from .settings import MEDIA_ROOT
from accounts import urls as accounts_urls

from blog import urls as blog_urls

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$', post_list, name='index'),
    url(r'^blog/', include(blog_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'documents_root': MEDIA_ROOT}),
    url(r'^user/',include(accounts_urls)),


]
