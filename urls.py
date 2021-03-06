from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': '/home/gen/users/pradeep/fun/images/'}),
    (r'^rate/$', 'rate.views.index'),
    (r'^rate/(?P<institute>[a-z]{4})/$', 'rate.views.institute'),
    (r'^rate/(?P<institute>[a-z]{4})/(?P<department>[a-z]{3})/$',
     'rate.views.inst_dept'),
    (r'^rate/(?P<department>[a-z]{3})/$', 'rate.views.department'),
    (r'^rate/(?P<id>\d+)/$', 'rate.views.prof_display'),
    (r'^rate/submit/(?P<id>\d+)/$', 'rate.views.submit'),
)
