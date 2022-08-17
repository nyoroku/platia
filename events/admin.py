from django.contrib import admin
from .models import Application, Blog, Latest
import csv
import datetime
from django.http import HttpResponse


class LatestAdmin(admin.ModelAdmin):
    list_filter = ('created', 'title', 'body')
    list_display = ('created', 'title', 'body')
    search_fields = ('created', 'title', 'body')
    date_hierarchy = 'created'
    ordering = ('created', 'created')
admin.site.register(Latest, LatestAdmin)






