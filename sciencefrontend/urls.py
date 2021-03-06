#Django required imports
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#Import pages
from scripts.home_content import *
from scripts.about import *
from scripts.scripts import *
from scripts.contact import *

#Import scripts
from scripts.xafs_sample_prep import *
from scripts.chemical_solutions import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	#Pages
	url(r'^$', home_content),
    url(r'^about/$', about),
    url(r'^scripts/$', scripts),
    url(r'^contact/$', contact),

	#Scripts
    url(r'^xafs_sample_prep/$', xafs_sample_prep),
    url(r'^xafs_sample_prep/abslen/$', xafs_sample_prep_get_abslen),

    url (r'^chemical_solutions/$', chemical_solutions),
    url (r'^chemical_solutions/compute/$', chemical_solutions_compute),

    # Examples:
    # url(r'^$', 'sciencefrontend.views.home', name='home'),
    # url(r'^sciencefrontend/', include('sciencefrontend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += patterns('',
 #       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
 #       'document_root': settings.MEDIA_ROOT}))