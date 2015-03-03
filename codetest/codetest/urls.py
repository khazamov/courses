from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.views.generic.base import TemplateView
import workshops
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'workshops.views.login_user', name='auth_login'),
    url(r'^login/$', 'workshops.views.login_user', name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
         'next_page': '/login'}, name='auth_logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^workshops/', include('workshops.urls')),




    #url(r'^workshops', include('workshops.urls',namespace='workshops')),
)
