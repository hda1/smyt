from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'smyt.views.index'),
    url(r'^json/(?P<model_name>[^/]*)/$', 'smyt.views.json'),
    url(r'^load$', 'smyt.views.load'),
    #url(r'^smyt/load', include('smyt.load')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
