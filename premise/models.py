# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from places.fields import PlacesField
from address.models import AddressField
from address.models import Address
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse

from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
import datetime
from smart_selects.db_fields import ChainedForeignKey

class User(AbstractUser):
    is_profile = models.BooleanField(default=False)
    is_finder = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    number = PhoneNumberField()
    picture = ProcessedImageField(upload_to='agents', processors=[ResizeToFill(200, 200)],
                                  format='JPEG',
                                  options={'quality': 100}, blank=True)
    logo = ProcessedImageField(upload_to='agents-logos', processors=[ResizeToFill(100, 100)],
                                  format='JPEG',
                                  options={'quality': 100}, blank=True)
    description = models.TextField(blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Type(models.Model):
    name = models.CharField(max_length=60)
    picture = ProcessedImageField(upload_to='writers', processors=[ResizeToFill(300, 300)],
                                  format='JPEG',
                                  options={'quality': 100}, blank=True)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ward(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County)

    def __str__(self):
        return self.name


class Category(models.Model):
    created = models.DateTimeField(auto_now=True)
    photo = ProcessedImageField(upload_to='attractions', processors=[ResizeToFill(512, 380)],
                                        format='JPEG',
                                        options={'quality': 100}, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = 'ServiceCategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('premise:category-detail', args=[
            self.slug])



class Property(models.Model):

    PURPOSE = (
        ('buy', 'BUY'),
        ('rent', 'RENT'),
        ('short stay', 'SHORT STAY'))

    AVAILABILITY = (
        ('yes', 'YES'),
        ('no', 'NO'))
    SPECIAL = (
        ('yes', 'YES'),
        ('no', 'NO'))
    FURNISHED = (
        ('yes', 'YES'),
        ('no', 'NO'))
    address = AddressField(related_name='address', blank=True, null=True)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField(default=1)
    amenities = models.TextField()
    county = models.ForeignKey(County, related_name='counties')
    availability = models.CharField(max_length=20, choices=AVAILABILITY, default='yes')
    purpose = models.CharField(max_length=50, choices=PURPOSE, default='rent')
    furnishing = models.CharField(max_length=50, choices=FURNISHED, default='no')
    special_offer = models.CharField(max_length=50, choices=SPECIAL, default='no')
    key_features = models.TextField()
    details = models.TextField()
    agent = models.ForeignKey(User, related_name='%(class)s_related')
    picture = ProcessedImageField(upload_to='properties', processors=[ResizeToFill(639, 426)],
                                  format='JPEG',
                                  options={'quality': 100})
    type = models.ForeignKey(Type, related_name='types')
    size = models.PositiveIntegerField()
    sponsored = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    finders = models.ManyToManyField(User, related_name='property_saved', blank=True)
    slug = models.SlugField()
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('premise:prop-detail', args=[self.created.year,
                                                 self.created.strftime('%m'),
                                                 self.created.strftime('%d'),
                                                 self.slug])


class Image(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images', processors=[ResizeToFill(1024, 767)],
                                format='JPEG',
                                options={'quality': 100})
    property = models.ForeignKey(Property, related_name='images')

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title


class Liked(models.Model):
    premise = models.ForeignKey(Property)
    finder = models.ForeignKey(User, related_name='properties_liked')
    date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return "%s liked by %s" % (self.premise, self.finder)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Liked, self).save(*args, **kwargs)


class Bookmark(models.Model):
    property = models.ForeignKey(Property)
    user = models.ForeignKey(User, related_name='properties_bookmarked')
    date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return "%s bookmarked by %s" % (self.property, self.user)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Bookmark, self).save(*args, **kwargs)


class Message(models.Model):
    name = models.CharField(max_length=100)
    premise = models.ForeignKey(Property)
    email = models.EmailField()
    phone = PhoneNumberField()
    message = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Message, self).save(*args, **kwargs)


class Service(models.Model):
    owner = models.ForeignKey(User, related_name='businesses')
    slug = models.SlugField(max_length=200, default='business')
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    phone = PhoneNumberField()
    created = models.DateTimeField(auto_now=True)
    county = models.ForeignKey(County)
    categories = models.ManyToManyField(Category, related_name='categories', blank=True)
    ward = ChainedForeignKey(
        Ward,
        chained_field="county",
        chained_model_field="county",
        show_all=False,
        auto_choose=False,
        sort=True)
    tag_line = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)
    photo = ProcessedImageField(upload_to='attractions', processors=[ResizeToFill(300, 200)],
                                format='JPEG',
                                options={'quality': 100}, blank=True)









