from mongoengine import Document, StringField, ReferenceField, ListField, DateTimeField

class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author, required=True)
    tags = ListField(StringField())
