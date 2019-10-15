from peewee import *

from .database import db


class User(Model):
    id = PrimaryKeyField()
    username = CharField(null=True)
    password = CharField(null=True)

    @property
    def get_data(self):
        return {'username':self.username,'password':self.password}

    def data(self):
        return {'username':self.username,'password':self.password}

    class Meta:
        database = db
        schema = 'public'


with db:
    User.create_table(fail_silently=True)