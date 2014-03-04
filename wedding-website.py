import cgi
import os

import jinja2
import json
import logging
import webapp2

from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.ext import db
from google.appengine.ext import deferred
from models import Guest

SHOW_GARBA_EVENT = 1
SHOW_CEREMONY_EVENT = 1
SHOW_RECEPTION_EVENT = 1

if (app_identity.get_application_id() == 'adiandjayodita'):
    SHOW_GARBA_EVENT = 0
if (app_identity.get_application_id() == 'adityawedsjayodita'):
    SHOW_GARBA_EVENT = 0
    SHOW_CEREMONY_EVENT = 0

event_template_values = {'SHOW_GARBA_EVENT' : SHOW_GARBA_EVENT,
                         'SHOW_CEREMONY_EVENT' : SHOW_CEREMONY_EVENT,
                         'SHOW_RECEPTION_EVENT' : SHOW_RECEPTION_EVENT}

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/welcome.html').render())

class HomePage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/home.html').render())

class StoryPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/story.html').render())

class EventsPage(webapp2.RequestHandler):
    def get(self):
        if SHOW_RECEPTION_EVENT and not SHOW_CEREMONY_EVENT and not SHOW_GARBA_EVENT:
            self.response.write(JINJA_ENVIRONMENT.get_template('templates/reception.html').render(event_template_values))
        else:
            self.response.write(JINJA_ENVIRONMENT.get_template('templates/events.html').render(event_template_values))

class GarbaPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/garba.html').render(event_template_values))

class CeremonyPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/ceremony.html').render(event_template_values))

class ReceptionPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/reception.html').render(event_template_values))
        
class GuestBookPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/guest_book.html').render())
        
class AccommodationsPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/accommodations.html').render())
        
class PhotosPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/photos.html').render())

class RSVPPage(webapp2.RequestHandler):
    def get(self):
        template_values = {'fill_out_rsvp_page_path' : '/filloutrsvp'}
        failure_reason = cgi.escape(self.request.get('failure_reason')) if self.request.get('failure_reason') else None
        if failure_reason:
            template_values['error_message'] = 'Sorry, that\'s not a valid login'
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/rsvp.html').render(template_values))
        
class RSVPThankyouPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/rsvp_thank_you.html').render())

class GuestState:
    NOT_INVITED, INVITED, NOT_ATTENDING, ATTENDING = range(4)

class FillOutRSVPPage(webapp2.RequestHandler):
    def post(self):
        group_name = cgi.escape(self.request.get('group_name'))
        group_name = group_name.lower()
        group_members = db.GqlQuery("SELECT * FROM Guest WHERE group_name = :1 order by first_name", group_name)
        if group_members.count() > 0:
            template_values = {'submit_rsvp_page_path' : '/submitrsvp',
                               'thank_you_page_path' : '/thankyou',
                               'group_name' : group_name,
                               'group_members' : group_members,
                               'STATE_NOT_INVITED' : GuestState.NOT_INVITED,
                               'STATE_INVITED' : GuestState.INVITED,
                               'STATE_NOT_ATTENDING' : GuestState.NOT_ATTENDING,
                               'STATE_ATTENDING' : GuestState.ATTENDING}
            self.response.write(JINJA_ENVIRONMENT.get_template('templates/fillout_rsvp.html').render(template_values))
        else:
            self.redirect('/rsvp?failure_reason=invalid_login')

class SubmitRSVPPage(webapp2.RequestHandler):
    def post(self):
        success_response = json.dumps({'success' : '1'})
        self.response.headers.add_header('content-type', 'application/json', charset='utf-8')

        group_name = cgi.escape(self.request.get('group_name')) if self.request.get('group_name') else None
        if group_name is None:
            success_response = json.dumps({'success' : '1'})
            self.response.out.write(success_response)

	group_members = db.GqlQuery('SELECT * FROM Guest WHERE group_name = :1', group_name)

        for group_member in group_members:
            key_identifier = group_member.key().id()

            filled_out_name_key = 'filled_out_name_' + str(key_identifier)
            filled_out_name = cgi.escape(self.request.get(filled_out_name_key)) if self.request.get(filled_out_name_key) else None
            if filled_out_name:
                group_member.filled_out_name = filled_out_name

            garba_key = 'garba_' + str(key_identifier)
            garba_response = cgi.escape(self.request.get(garba_key)) if self.request.get(garba_key) else None
            if garba_response:
                group_member.garba = int(garba_response)

            ceremony_key = 'ceremony_' + str(key_identifier)
            ceremony_response = cgi.escape(self.request.get(ceremony_key)) if self.request.get(ceremony_key) else None
            if ceremony_response:
                group_member.ceremony = int(ceremony_response)

            reception_key = 'reception_' + str(key_identifier)
            reception_response = cgi.escape(self.request.get(reception_key)) if self.request.get(reception_key) else None
            if reception_response:
                group_member.reception = int(reception_response)

            group_member.put()

        deferred.defer(send_confirmation_email, group_name)

        self.response.out.write(success_response)

def send_confirmation_email(group_name):
    sender_address = 'admin@%s.appspotmail.com' % app_identity.get_application_id()
    recepient_address = 'jayodita@gmail.com'
    subject = 'Received RSVP from %s' % group_name
    body = ''

    group_members = db.GqlQuery('SELECT * FROM Guest WHERE group_name = :1 order by first_name, filled_out_name', group_name)

    for group_member in group_members:
        if group_member.filled_out_name is not None:
           body += '%s: ' % group_member.filled_out_name
        else:
           body += '%s %s: ' % (group_member.first_name, group_member.last_name)
        if group_member.garba == GuestState.ATTENDING:
           body += 'Garba '
        if group_member.ceremony == GuestState.ATTENDING:
           body += 'Ceremony '
        if group_member.reception == GuestState.ATTENDING:
           body += 'Reception'
        body += '\n'

    mail.send_mail(sender_address, recepient_address, subject, body)

class GetAllRSVPsPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('content-type', 'text/plain', charset='utf-8')
        deferred.defer(send_full_rsvp_list_email)
        self.response.out.write('Emails sent to the site admins!')

def send_full_rsvp_list_email():
    sender_address = 'admin@%s.appspotmail.com' % app_identity.get_application_id()
    recepient_address = 'aditya.rathnam@gmail.com, jayodita@gmail.com'
    subject = 'Full RSVP List from %s' % app_identity.get_application_id()
    body = ''

    group_members = db.GqlQuery('SELECT * FROM Guest order by group_name, first_name')

    for group_member in group_members:
        body += '%s,%s,%s,%s,%d,%d,%d\n' % (group_member.first_name, group_member.last_name, group_member.group_name, \
                                            group_member.filled_out_name.strip(',') if group_member.filled_out_name is not None else '', \
                                            group_member.garba, group_member.ceremony, group_member.reception)

    mail.send_mail(sender_address, recepient_address, subject, body)

application = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/home', HomePage),
    ('/story', StoryPage),
    ('/events', EventsPage),
    ('/garba', GarbaPage),
    ('/ceremony', CeremonyPage),
    ('/reception', ReceptionPage),
    ('/guest_book', GuestBookPage),
    ('/photos', PhotosPage),
    ('/accommodations', AccommodationsPage),
    ('/rsvp', RSVPPage),
    ('/filloutrsvp', FillOutRSVPPage),
    ('/submitrsvp', SubmitRSVPPage),
    ('/thankyou', RSVPThankyouPage),
    ('/getallrsvp', GetAllRSVPsPage),
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
