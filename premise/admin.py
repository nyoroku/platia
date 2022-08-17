# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Profile, Property, Type, Image, County, Category, Ward
from address.models import AddressField
from address.forms import AddressWidget


class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('user', 'company')
    list_display = ('user', 'company')
    search_fields = ('user', 'company')
admin.site.register(Profile, ProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created')
    list_display = ('name', 'created')
    search_fields = ('name', 'created')
    date_hierarchy = 'created'
    ordering = ('created',)
admin.site.register(Category, CategoryAdmin)


class CountyAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(County, CountyAdmin)

class WardAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Ward, WardAdmin)

class PropertyAdmin(admin.ModelAdmin):
    list_filter = ('name', 'price')
    list_display = ('name', 'price')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('price', 'name', 'address')
    formfield_overrides = {
        AddressField: {
            'widget': AddressWidget(
                attrs={
                    'style': 'width: 300px;'
                }
            )
        }
    }


admin.site.register(Property, PropertyAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
admin.site.register(Type, TypeAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_filter = ('title', 'date_added')
    list_display = ('title', 'image')
    search_fields = ('date_added', 'title')
    date_hierarchy = 'date_added'
    ordering = ('date_added',)
admin.site.register(Image, ImageAdmin)