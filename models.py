import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Guest(db.Model):
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    group_name = db.StringProperty(required=True)
    filled_out_name = db.StringProperty(required=False)
    garba = db.IntegerProperty(required=True)
    ceremony = db.IntegerProperty(required=True)
    reception = db.IntegerProperty(required=True)
