import json
import db_connection
from datetime import datetime
from models import Author, Quote


def read_upload_authors():
    with open(file='authors.json', mode='r', encoding='utf-8') as file:
        authors = json.load(file)

        for author in authors:
            existing_author = Author.objects.filter(fullname=author['fullname']).first()

            if not existing_author:
                born_date = datetime.strptime(author['born_date'], "%B %d, %Y")
                Author(
                    fullname=author['fullname'],
                    born_date=born_date,
                    born_location=author['born_location'],
                    description=author['description']
                ).save()


def read_upload_quotes():
    with open(file='quotes.json', mode='r', encoding='utf-8') as file:
        quotes = json.load(file)

        for quote in quotes:
            author_name = quote['author']
            author = Author.objects.filter(fullname=author_name).first()

            if author:
                existing_quote = Quote.objects.filter(quote=quote['quote'], author=author).first()

                if not existing_quote:
                    Quote(
                        tags=quote['tags'],
                        author=author,
                        quote=quote['quote']
                    ).save()


