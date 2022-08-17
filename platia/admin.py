from django.contrib import admin
from .models import Trip, Category, Image


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('title', 'date_added')
    list_display = ('title', 'detail')
    search_fields = ('date_added', 'title')
    date_hierarchy = 'date_added'
    ordering = ('date_added',)
admin.site.register(Category, CategoryAdmin)


class TripAdmin(admin.ModelAdmin):
    list_filter = ('title', 'date_added', 'price', 'availability', )
    list_display = ('title', 'availability', 'start', 'End', 'slug', 'price', 'summary',
                    'included',
                    'excluded', 'photo'
                    )
    search_fields = ('date_added', 'title')
    date_hierarchy = 'date_added'
    ordering = ('date_added',)
admin.site.register(Trip, TripAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_filter = ('title', 'date_added')
    list_display = ('title', 'image')
    search_fields = ('date_added', 'title')
    date_hierarchy = 'date_added'
    ordering = ('date_added',)
admin.site.register(Image, ImageAdmin)


