from django.conf.urls import url, patterns, include

urlpatterns = patterns('',


        url(r'^$', 'workshops.views.index', name='index'),
        url(r'^(?P<workshop_id>\d+)/remove_result/$', 'workshops.views.remove_result', name='remove_result'),
        url(r'^(?P<workshop_id>\d+)/add_result/$', 'workshops.views.add_result', name='result'),
        url(r'^accounts/profile/$', 'workshops.views.profile', name='profile'),

)