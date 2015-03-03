from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='start.html')),
    url(r'^login/$', 'workshops.views.login_user', name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
         'next_page': '/login'}, name='auth_logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^workshops/$', 'workshops.views.index', name='index'),
    url(r'^accounts/profile/$', 'workshops.views.profile', name='profile'),
    url(r'^workshops/(?P<workshop_id>\d+)/result/$', 'workshops.views.result', name='result'),

    #url(r'^workshops', include('workshops.urls',namespace='workshops')),
)
