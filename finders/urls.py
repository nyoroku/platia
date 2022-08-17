from django.conf.urls import url
from . import views
app_name = 'finders'


urlpatterns = [
    url(r'^user_register/$', views.FinderRegistrationView.as_view(), name='user_registration'),
    url(r'^agent_register/$', views.AgentRegistrationView.as_view(), name='agent_registration'),
    url(r'^common/$', views.common_view, name='common'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^profile/$', views.profile, name='profile'),
]