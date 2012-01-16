# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
#from lizard_ui.urls import debugmode_urlpatterns

import lizard_kpi.views

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$',
        lizard_kpi.views.kpi_pages,
        name="lizard_kpi_pages"),
    url(r'^(?P<page>.+)/$',
        lizard_kpi.views.gauges,
        name="lizard_kpi_gauges"),
    )
#urlpatterns += debugmode_urlpatterns()
# ^^^ TODO. Lizard 3.0...
