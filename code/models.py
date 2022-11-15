from peewee import Model, CharField, TextField, DateField,\
    SqliteDatabase, BooleanField, ForeignKeyField
    
from datetime import datetime

database = SqliteDatabase("Post.db")


class BaseModels(Model):
    created_time = DateField(default=datetime.now())

    class Meta():
        database = database


class Category(BaseModels):
    name = CharField()


class Articles(BaseModels):
    url = CharField()

    body = TextField(null=True)
    title = CharField(null=True)
    is_completed = BooleanField(default=False)

    category = ForeignKeyField(Category, backref="Articles")
