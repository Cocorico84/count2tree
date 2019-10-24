from peewee import *

from .database import db


class Tree(Model):
    id = PrimaryKeyField()
    localisation = CharField(null=True)
    genus = CharField(null=True)
    specie = CharField(null=True)
    variety = CharField(null=True)
    height = FloatField(null=True)


    class Meta:
        database = db
        schema = 'public'

    @property
    def caracteristics(self):
        return {'variety':self.variety,'height':self.height}

    def get_small_data(self):
        return {'genus': self.genus, 'specie': self.specie, 'variety': self.variety,'height': self.height,'location':self.localisation,'id':self.id}

with db:
    Tree.create_table(fail_silently=True)