#Django required imports
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#Import scripts
from scripts.home_content import *
from scripts.function_plot import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	#Pages
	url(r'^$', home_content),

	#Scripts
	url(r'^function_plot/$', function_plot),
	url(r'^function_plot/plot\.(?P<type>.+)$', function_plot_image),
	url(r'^function_plot/submit/$', function_plot_submit),


    # Examples:
    # url(r'^$', 'sciencefrontend.views.home', name='home'),
    # url(r'^sciencefrontend/', include('sciencefrontend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()