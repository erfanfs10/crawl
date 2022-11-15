from models import Articles, Category, database


def create_db():
    database.create_tables([Articles, Category])
