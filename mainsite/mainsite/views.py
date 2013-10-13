from django.http import HttpResponse
from django.shortcuts import render_to_response

    url(r'^$', 'mainsite.views.welcome'),
    url(r'^home$', 'mainsite.views.home'),
    url(r'^story$', 'mainsite.views.story'),
    url(r'^events$', 'mainsite.views.events'),
    url(r'^events/garba$', 'mainsite.views.events_garba'),
    url(r'^events/ceremony$', 'mainsite.views.events_ceremony'),
    url(r'^events/reception$', 'mainsite.views.events_reception'),
    url(r'^accommodations$', 'mainsite.views.accommodations'),
    url(r'^rsvp$', 'mainsite.views.rsvp'),
    url(r'^guestbook$', 'mainsite.views.guestbook'),
    url(r'^photos$', 'mainsite.views.photos'),

def welcome(request):
    return render_to_response('welcome.html', {'mixpanel_api_token': settings.MIXPANEL_API_TOKEN},
                                  context_instance=RequestContext(request))

def download(request):
    return render_to_response_pre('download.html', {'mixpanel_api_token': settings.MIXPANEL_API_TOKEN},
                                  context_instance=RequestContext(request))

def documentation(request):
    return render_to_response_pre('documentation.html', {'mixpanel_api_token': settings.MIXPANEL_API_TOKEN},
                                  context_instance=RequestContext(request))

def about(request):
    return render_to_response_pre('about.html', {'mixpanel_api_token': settings.MIXPANEL_API_TOKEN},
                                  context_instance=RequestContext(request))

def terms(request):
    return render_to_response_pre('terms.html', {'mixpanel_api_token': settings.MIXPANEL_API_TOKEN},
                                  context_instance=RequestContext(request))

def privacy(request):
    return render_to_response_pre('privacy.html', {'mixpanel_api_token': settings.MIXPANEL_API_TOKEN},
                                  context_instance=RequestContext(request))
