from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
           url(r'^apply/$', views.apply_course, name='apply'),
           url(r'^blog/$', views.blog_list, name='blog'),
           url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/' \
           r'(?P<blog>[-\w]+)/$',
           views.blog_detail,
           name='blog-detail'),

           url(r'^allevents/$', views.allevents, name='allevents'),

]
