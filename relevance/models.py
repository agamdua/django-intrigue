from django.db import models


class JSONStore(models.Model):
    """
    This model's primary purpose is to serve as a store
    for JSON as strings in the database.

    Let's pretend that we don't have any control over these: we receive these
    from an external API which we cannot change.

    The general format of a JSON one would receive from this service is:

        {'books': {
            'genres': [{
                'fantasy': {
                    'WoT': ['Robert Jordan', 'Brandon Sanderson'],
                    'Mistborn': ['Brandon Sanderson'],
                    'The Hobbit': ['J.R.R. Tolkein'],
                }
            }]
        }}

    It will be stored in the DB as a string like:
        '{'books': {'genres': [{'fantasy': {'WoT': ['Robert Jordan', 'Brandon Sanderson'],'Mistborn': ['Brandon Sanderson'],'The Hobbit': ['J.R.R. Tolkein']}}]}}' # noqa

    PEP8 has been deliberately violated to emphasize the structure of the data
    that will be stored in the db as a string.

    Aside:
        Yes, Postgres does have a JSON Field, but not all of us are lucky
        enough to be _paid_ to work on a Django/Postgres stack.
    """
    books = models.TextField()
