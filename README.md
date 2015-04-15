# bcx-python

bcx-python is a console client wrapper for the APIREST from from [Basecamp](https://basecamp.com/) with the initial scope of implementing only the GET functions. I'm actually developing it because I want to have a way to manage my own dashboard and analyze the data in a different way, because until now I haven't found a good functionality out there.

## Dependencies

*  [``requests``](http://python-requests.org)

## Implemented

Until now I only implemented the following calls:

* [projects](https://github.com/basecamp/bcx-api/blob/master/sections/projects.md)
* [people](https://github.com/basecamp/bcx-api/blob/master/sections/people.md)

## TODO's
-----

* Implement CLI-Interface through a nice command line client.
* Create documentation - maybe
* Implement a better exception handling for the requests.
* Implement the following API calls:
```
Project Templates
Stars
Accesses
Companies/Groups
Events
Topics
Messages
Comments
Todo lists
Todos
Documents
Attachments
Uploads
Calendars
Calendar events
```
