import os

import jinja2
import webapp2

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

application = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/home', HomePage),
    ('/story', StoryPage),
    ('/events', EventsPage),
    ('/garba', GarbaPage),
    ('/ceremony', CeremonyPage),
    ('/reception', ReceptionPage),
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
