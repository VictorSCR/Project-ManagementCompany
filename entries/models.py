from django.db import models
from django.utils import timezone
from django.views.generic import ListView




class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"

class Mylist(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class News(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()

class Base(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()

class Contacts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
