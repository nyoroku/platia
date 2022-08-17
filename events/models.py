from __future__ import unicode_literals
from datetime import datetime
import datetime
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Application(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    course = models.CharField(max_length=80)
    qualification = models.CharField(max_length=20, verbose_name='academic qualification', default='N/A')
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    applied = models.DateTimeField(auto_now_add=True, verbose_name='applied on')
    aboutus = models.TextField(blank=True, verbose_name='how did you find out about us?')

    class Meta:
        ordering = ('-applied',)

    def __str__(self):
        return self.firstname


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self
                     ).get_queryset()\
            .filter(status='published')


class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.CharField(max_length=200)
    overview = models.TextField(blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:blog-detail', args=[self.publish.year,
                                                      self.publish.strftime('%m'),
                                                      self.publish.strftime('%d'),
                                                      self.slug])


class Latest(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique_for_date='created', default='latest')
    photo = ProcessedImageField(upload_to='latest', processors=[ResizeToFill(539, 303)],
                                format='JPEG',
                                options={'quality': 100}, blank=True)
    day = models.DateField(verbose_name='Event Day')
    start = models.TimeField()
    end = models.TimeField()


    class Meta:
        ordering = ('-created',)
        verbose_name = 'Events Happening'
        verbose_name_plural = 'Events Happening'

    def __str__(self):
        return self.title






