import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Guest(db.Model):
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    group_name = db.StringProperty(required=True)
    attending_garba = db.IntegerProperty(required=True)
    attending_ceremony = db.IntegerProperty(required=True)
    attending_reception = db.IntegerProperty(required=True)
