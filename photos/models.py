from  __future__ import unicode_literals

from django.db import models

# Create your models here.

class Photos(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    tag = models.CharField(max_length=20, default='')
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name