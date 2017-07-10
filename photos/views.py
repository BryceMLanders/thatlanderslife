from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Photos
from rest_framework import viewsets
from django.template.context_processors import csrf

# Create your views here.


def all_photos(request):
    photos = Photos.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "photos.html", {"photos": photos}, args)

def photos_by_tags(request):
    photos = Photos.objects.filter(published_date__lte=timezone.now()).order_by('-tag')
    args = {}
    args.update(csrf(request))
    return render(request, "photos.html", {"photos": photos}, args)

def photos_by_ireland(request):
    photos = Photos.objects.filter(tag = 'ireland')
    args = {}
    args.update(csrf(request))
    return render(request, "photos.html", {"photos": photos}, args)

def photos_by_girls(request):
    photos = Photos.objects.filter(tag = 'girls')
    args = {}
    args.update(csrf(request))
    return render(request, "photos.html", {"photos": photos}, args)

def photos_by_van(request):
    photos = Photos.objects.filter(tag = 'van')
    args = {}
    args.update(csrf(request))
    return render(request, "photos.html", {"photos": photos}, args)

def photos_by_friends(request):
    photos = Photos.objects.filter(tag = 'friends')
    args = {}
    args.update(csrf(request))
    return render(request, "photos.html", {"photos": photos}, args)