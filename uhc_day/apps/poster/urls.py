from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'poster.views.overlay', name="poster-overlay"),
    url(r'^grid/$', 'poster.views.grid', name="poster-grid"),
)