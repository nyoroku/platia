from django.conf.urls import url
from . import views
from .views import premise, platia, CountyAutocomplete


app_name = 'premise'
urlpatterns = [
    url(r'^premise/', premise, name='premise'),
    url(r'^allpremises/', views.all_premises, name='allpremises'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.all_premises,
          name='allpremises_by_tag'),
    url(r'^flats/', views.flat, name='flats'),
    url(r'^condos/', views.condos, name='condos'),
    url(r'^commercials/', views.commercial, name='commercials'),
    url(r'^multifamily/', views.multi_family, name='multifamily'),
    url(r'^townhouse/', views.townhouse, name='townhouses'),
    url(r'^rent/', views.rents, name='rent'),
    url(r'^buy/', views.buy, name='buy'),
    url(r'^shortstay/', views.short_stay, name='shortstay'),
    url(r'^nicosia-rent/', views.nicosia_rent, name='nicosiarent'),
    url(r'^famagusta-rent/', views.famagusta_rent, name='famagustarent'),
    url(r'^limassol-rent/', views.limassol_rent, name='limassolrent'),
    url(r'^larnaca-rent/', views.larnaca_rent, name='larnacarent'),
    url(r'^paphos-rent/', views.paphos_rent, name='paphosrent'),
    url(r'^kyrenia-rent/', views.kyrenia_rent, name='kyreniarent'),
    url(r'^nicosia-buy/', views.nicosia_buy, name='nicosiabuy'),
    url(r'^famagusta-buy/', views.famagusta_buy, name='famagustabuy'),
    url(r'^limassol-buy/', views.limassol_buy, name='limassolbuy'),
    url(r'^larnaca-buy/', views.larnaca_buy, name='larnacabuy'),
    url(r'^paphos-buy/', views.paphos_buy, name='paphosbuy'),
    url(r'^kyrenia-buy/', views.kyrenia_buy, name='kyreniabuy'),
    url(r'^nicosia-short/', views.nicosia_short, name='nicosiashort'),
    url(r'^famagusta-short/', views.famagusta_short, name='famagustashort'),
    url(r'^limassol-short/', views.limassol_short, name='limassolshort'),
    url(r'^larnaca-short/', views.larnaca_short, name='larnacashort'),
    url(r'^paphos-short/', views.paphos_short, name='paphosshort'),
    url(r'^kyrenia-short/', views.kyrenia_short, name='kyreniashort'),

    url(r'^prop/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/' 
           r'(?P<prop>[-\w]+)/$',
           views.property_detail,
           name='prop-detail'),

    url(r'^platia/', platia, name='platia'),

    url(r'^results/', views.search, name='search'),
    url(r'^mine/$', views.ManagePropertyListView.as_view(), name='my_list'),
    url(r'^create/$', views.PropertyCreateView.as_view(), name='property_add'),
    url(r'^(?P<pk>\d+)/edit/$', views.PropertyUpdateView.as_view(), name='property_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.PropertyDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/image/$', views.PropertyImageUpdateView.as_view(), name='property_image_update'),
    url(r'^save/$', views.add_bookmark,
        name='save'),
    url(r'^my_save/$', views.BookmarkListView.as_view(), name='my_save'),
    url(r'^about-us/', views.about, name='about'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^message_agent/(?P<premise_id>\d+)/$', views.message_agent, name='message_agent'),
    url(r'^message/', views.message_list, name='message_list'),
    url(
        r'^county-autocomplete/$',
        CountyAutocomplete.as_view(),
        name='county-autocomplete',
    ),
    url(r'^my_services/$', views.ManageServiceListView.as_view(), name='my_services'),
    url(r'^create_service/$', views.ServiceCreateView.as_view(), name='service_add'),
    url(r'^(?P<pk>\d+)/service_edit/$', views.SericeUpdateView.as_view(), name='service_edit'),
    url(r'^(?P<pk>\d+)/delete_service/$', views.ServiceDeleteView.as_view(), name='service_delete'),
    url(r'^category/(?P<categories>[-\w]+)/$',
        views.category_detail,
        name='category-detail')
]