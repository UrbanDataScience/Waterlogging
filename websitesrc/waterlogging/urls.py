from django.conf.urls import patterns, include, url
from waterlogging import settings, views
from register.views import reg_table, sendMsg
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'waterlogging.views.index', name='index'),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    url(r'^graph/$', views.graph),
    url(r'^register/$', reg_table),
    url(r'^send/$', sendMsg),
    # Examples:
    # url(r'^$', 'waterlogging.views.home', name='home'),
    # url(r'^waterlogging/', include('waterlogging.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
