from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^homebase/', include('homebase.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Links to login 
urlpatterns += patterns('',
	url(r'^dashboard/login/$',  login, name='login'),
    url(r'^dashboard/logout/$', logout, name='logout'),
)