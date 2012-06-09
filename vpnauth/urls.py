from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin 
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$','vpnauth.vpn.views.index'),
    (r'^admin/', include(admin.site.urls)),

)
