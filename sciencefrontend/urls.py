from django.conf.urls import patterns, include, url
from sciencefrontend.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^function_plot_png/(?P<funct>.+)/(?P<arg>.+)/(?P<xmin>-?\d+)/(?P<xmax>-?\d+)/(?P<ymin>-?\d+)/(?P<ymax>-?\d+)/(?P<xlabel>\w+)/(?P<ylabel>\w+)/plot\.png$', function_plot_png),
    # Examples:
    # url(r'^$', 'sciencefrontend.views.home', name='home'),
    # url(r'^sciencefrontend/', include('sciencefrontend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()