from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from .views import IndexView, JsonView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^json/(?P<model_name>[^/]*)/$', JsonView.as_view()),
    #url(r'^json/(?P<model_name>[^/]*)/$', IndexView.as_view(), name='home2'),
    #url(r'^load$', 'smyt.views.load'),
    #url(r'^smyt/load', include('smyt.load')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
