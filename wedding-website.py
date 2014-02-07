import cgi
import os

import jinja2
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

class FillOutRSVPPage(webapp2.RequestHandler):
    def post(self):
        group_name = cgi.escape(self.request.get('group_name'))
        group_members = db.GqlQuery("SELECT * FROM Guest WHERE group_name = :1", group_name)
        template_values = {'group_members' : group_members}
        self.response.write(JINJA_ENVIRONMENT.get_template('templates/fillout_rsvp.html').render(template_values)) 

class ConfirmRSVPPage(webapp2.RequestHandler):
    def post(self):
       pass

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
    ('/confirmrsvp', ConfirmRSVPPage), 
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
