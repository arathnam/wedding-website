import cgi
import os

import jinja2
import json
import logging
import webapp2

from google.appengine.ext import db
from models import Guest

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
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/events.html').render())

class GarbaPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/garba.html').render())

class CeremonyPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/ceremony.html').render())

class ReceptionPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/reception.html').render())
        
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
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/rsvp.html').render(template_values))
        
class RSVPThankyouPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/rsvp-thankyou.html').render())

class GuestState:
    NOT_INVITED, INVITED, NOT_ATTENDING, ATTENDING = range(4)

class FillOutRSVPPage(webapp2.RequestHandler):
    def post(self):
        group_name = cgi.escape(self.request.get('group_name'))
        group_members = db.GqlQuery("SELECT * FROM Guest WHERE group_name = :1", group_name)
        template_values = {'submit_rsvp_page_path' : '/submitrsvp',
                           'group_name' : group_name,
                           'group_members' : group_members,
                           'STATE_NOT_INVITED' : GuestState.NOT_INVITED,
                           'STATE_INVITED' : GuestState.INVITED,
                           'STATE_NOT_ATTENDING' : GuestState.NOT_ATTENDING,
                           'STATE_ATTENDING' : GuestState.ATTENDING}
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/fillout_rsvp.html').render(template_values)) 

class SubmitRSVPPage(webapp2.RequestHandler):
    def post(self):
        success_response = json.dumps({'success' : '1'})
        self.response.headers.add_header('content-type', 'application/json', charset='utf-8')

        group_name = cgi.escape(self.request.get('group_name')) if self.request.get('group_name') else None
        if group_name is None:
            success_response = json.dumps({'success' : '1'})
            self.response.out.write(success_response)

	group_members = db.GqlQuery("SELECT * FROM Guest WHERE group_name = :1", group_name)

        for group_member in group_members:
            key_identifier = group_member.key().id()

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

        self.response.out.write(success_response)

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
    ('/rsvp-thankyou', RSVPThankyouPage)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
