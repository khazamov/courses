Welcome to the NOLS programmer code test.

This task is taken from a requirement we have implemented. 

NOLS offers workshops as part of an online registration for a
conference. Conference attendees can choose to participate in
zero, one or more workshops. 

Your primary task is to display a list of workshops and store
a user's selected workshops in the database. When done, land
the user on a simple success page. You can ignore payment,
applying for the actual conference and anything else not
directly related to storing selected workshops. Each selection
should be stored in a Registration object, with a foreign key
to a User (from django.contrib.auth) and a foreign key to the
selected Workshop. 

Lastly, the user should not be allowed to choose workshops that
overlap. All workshops have one of the following start/end times:

    * 8 am to noon (half day)
    * 1 pm to 5 pm (half day)
    * 8 am to 5 pm (one day)
    * 8 am to 5 pm (multiple, contiguous days)

You can assume that the number of workshops will always be less
than a dozen. The best solution will be the most readable, not
necessarily the one that would perform best with thousands of
potential workshop conflicts.

Software:
    * Use Python 2.7 or greater
    * Use SQLite for the backend
    * Use Django 1.6.5 or greater

We've provided you with a project with settings as well as basic
login urls and templates. We have also provided an initial_data.json
file that contains the workshop data. Your solution may use some or all of the model attributes.
Use the Python interpreter or Django's admin tool to create test
users (by-passing the need for registration forms and such).

Feel free to add improvements you feel are necessary. However, this
is the real world. Anything beyond the essential, obvious or trivial
requires input from the project owner. Be ready to discuss improvements:
what is the problem you're trying to solve, how would you solve it and
how long might it take.

Email steve_smith@nols.edu if any of these instructions are unclear; 
however, please take the initiative to make what you think are
appropriate decisions to move the solution forward. Think of this as a
proof-of-concept from which to start a conversation with the project 
owner.

Quickstart:
pip install -r requirements.txt
cd codetest
python manage.py syncdb
python manage.py runserver
