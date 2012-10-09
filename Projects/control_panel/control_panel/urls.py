from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pages.views.home'),
#    url(r'^Projects/', 'pages.views.listing'),
    url(r'^Projects/(?P<dir>([a-zA-Z0-9,\-,_,\.]*/)*)$', 'pages.views.listing'),
    url(r'^library/(books/)?$','pages.views.book'),
    url(r'^library/books/(?P<N>([0-9])*/)$', 'pages.views.bookinfo'),
    url(r'^library/authors/$','pages.views.author'),
    url(r'^library/authors/(?P<N>([0-9])*/)$', 'pages.views.authorinfo')
    # Examples:
    # url(r'^$', 'control_panel.views.home', name='home'),
    # url(r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
