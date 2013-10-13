from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # External Website
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'welcome.html'}),
    url(r'^home$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    url(r'^story$', 'django.views.generic.simple.direct_to_template', {'template': 'story.html'}),
    url(r'^events$', 'django.views.generic.simple.direct_to_template', {'template': 'events.html'}),
    url(r'^events/garba$', 'django.views.generic.simple.direct_to_template', {'template': 'garba.html'}),
    url(r'^events/ceremony$', 'django.views.generic.simple.direct_to_template', {'template': 'ceremony.html'}),
    url(r'^events/reception$', 'django.views.generic.simple.direct_to_template', {'template': 'reception.html'}),
    url(r'^accommodations$', 'django.views.generic.simple.direct_to_template', {'template': 'accommodations.html'}),
    url(r'^rsvp$', 'django.views.generic.simple.direct_to_template', {'template': 'rsvp.html'}),
    url(r'^guestbook$', 'django.views.generic.simple.direct_to_template', {'template': 'guestbook.html'}),
    url(r'^photos$', 'django.views.generic.simple.direct_to_template', {'template': 'photos.html'}),
)

urlpatterns += staticfiles_urlpatterns()
