import datetime
from google.appengine.ext import db
from google.appengine.tools import bulkloader
import models

class GuestLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Guest',
                                   [('last_name', lambda x: x.decode('utf-8')),
                                    ('first_name', lambda x: x.decode('utf-8')),
                                    ('group_name', lambda x: x.decode('utf-8').lower()),
                                    ('garba', int),
                                    ('ceremony', int),
                                    ('reception', int),
                                   ])

loaders = [GuestLoader]

