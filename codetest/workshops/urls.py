from django.conf.urls import url, patterns, include

urlpatterns = patterns('',
                       url(r'^$', 'workshops.views.index'),
                       url(r'^/profile/$', 'workshops.views.profile',name='profile'),

)