from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    # url(r'^$', 'psychology.views.home', name='home'),
    url(r'^game/$', 'psychology.game.views.game', name='game'),
    url(r'^level/(?P<level_id>\d+)/$', 'psychology.game.views.level', name='levels'),
    url(r'^answer/(?P<level_id>\d+)/$', 'psychology.game.views.answer', name='answer'),
    url(r'^hint/(?P<hint_id>\d+)/$', 'psychology.game.views.hint', name='hint'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    url(r'^admin/', include(admin.site.urls)),
)

