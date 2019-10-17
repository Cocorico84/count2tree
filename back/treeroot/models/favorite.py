from peewee import *

from .database import db


class Favorite(Model):
    id = PrimaryKeyField()
    genus = CharField(null=True)
    specie = CharField(null=True)
    variety = CharField(null=True)

    @property
    def data(self):
        return {'genus':self.genus,'specie':self.specie, 'variety':self.specie}

    class Meta:
        database = db
        schema = 'public'


with db:
    Favorite.create_table(fail_silently=True)