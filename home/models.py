from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name_plural = 'Categories'

    def __unicode__(self):
            return unicode(self.title)


class Writer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    picture = ProcessedImageField(upload_to='writers', processors=[ResizeToFill(100, 100)],
                                          format='JPEG',
                                          options={'quality': 100}, blank=True)

    def __unicode__(self):
        return unicode(self.name)


class Latest(models.Model):
    STATUS = (
        ('published', 'PUBLISHED'),
        ('draft', 'DRAFT'))
    PRIORITY = (
        ('yes', 'YES'),
        ('no', 'NO'))
    title = models.CharField(max_length=200)
    story = models.TextField()
    created = models.DateField(auto_now_add=True)
    summary = models.TextField()
    slug = models.SlugField(unique_for_date='created', default='latest')
    photo = ProcessedImageField(upload_to='latest', processors=[ResizeToFill(1778, 1000)],
                                          format='JPEG',
                                          options={'quality': 100}, blank=True)
    thumbnail = ProcessedImageField(upload_to='latest', processors=[ResizeToFill(100, 100)],
                                          format='JPEG',
                                          options={'quality': 100}, blank=True)
    category = models.ForeignKey(Category)
    writer = models.ForeignKey(Writer)
    status = models.CharField(max_length=50, choices=STATUS, default='draft')
    tags = TaggableManager()
    priority = models.CharField(max_length=50, choices=PRIORITY, default='no')
    video = models.URLField(blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return unicode(self.title)

    def get_absolute_url(self):
        return reverse('home:news', args=[self.created.year,
                                          self.created.strftime('%m'),
                                          self.created.strftime('%d'),
                                          self.slug])


class Testimonial(models.Model):
    title = models.CharField(max_length=50, blank=True)
    body = models.TextField()
    photo = ProcessedImageField(upload_to='latest', processors=[ResizeToFill(200, 150)],
                                format='JPEG',
                                options={'quality': 100}, blank=True)
    person = models.CharField(verbose_name='Testimonial From', blank=True, max_length=50)
    course = models.CharField(blank=True, max_length=50)


class Display(models.Model):
    title = models.CharField(max_length=50, blank=True)
    body = models.TextField()
    photo = ProcessedImageField(upload_to='latest', processors=[ResizeToFill(780, 354)],
                                format='JPEG',
                                options={'quality': 100}, blank=True)





