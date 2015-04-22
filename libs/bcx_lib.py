# -*- coding:utf-8 -*-

"""
Created on 2015-04-12
@requires: Python 3.4+
@summary:   Basecamp command line main lib to query the service API.
            This library does not implement CRUD with the API, it only makes
            GET calls.
@note:		This client works with basic authentication, the OAuth
            authentication is not implemented, mainly due to my interest in a
            tool that allows me to extract information to create my own
            dashboard and reporting tool, because basecamp has none, and in it's
            origin, the tool is conceived as an individual usage tool.
@author: Sebastian Reyes Espinosa
@contact: sebaslander@gmail.com
"""

import requests
import sys

__author__ = 'Sebastian Reyes Espinosa'
__email__ = 'sebaslander@gmail.com'
__creation_date__ = '2015-04-12'


class Basecamp():

    def __init__(self, user_id, username, password, company):
        """
        Construct of the main class, containing the initial components of the
        API, needed across every communication and obligatory to implement.

        @requires: user_id - main id code to reference the account admin
        @requires: username - user's registration name to acces Basecamp
        @requires: password - user's password
        @requires: company - app name
        """

        self.base_url = 'https://basecamp.com/{0}/api/v1/'.format(user_id)
        self.user_id = user_id
        self.username = username
        self.password = password
        self.company = company
        self.headers = {'User-Agent': '{0}:({1})'.format(company, username)}
        self.auth = (username, password)

    def set_connection(self, path):
        mod_url = self.base_url + path
        try:
            return requests.get(mod_url, headers=self.headers,
                                auth=self.auth)

        except Exception as e:
            print('Error de conexion\n', e)
            sys.exit(1)

    def query_projects(self, arg):
        """
        Invoques from the API a list of all projects into the platform and
        returns the context in a JSON file, accordingly to the selected option:

        API Calls implemented:

            /projects.json returns all active projects.
            /projects/drafts.json returns all draft projects.
            /projects/archived.json returns all archived projects.

        @requires: arg INT type value to signal the index of choice in args
                tuple args = ['projects', 'projects/drafts', 'projects/archived']
        @returns: JSON object
        """
        args = ['projects', 'projects/drafts', 'projects/archived']
        return self.set_connection('{0}.json'.format(args[arg])).json()

    def detailed_project(self, proj_id):
        """
        Invoques from the API the detail of the proj_id provided to the client
        and returns the context in a JSON file.

        API Calls implemented:

            /projects/1.json returns a detailed report of the specified project

        @requires: proj_id - INT type value equal to the 'id' identifier.
        @returns: JSON object
        """

        return self.set_connection('projects/{0}.json'.format(proj_id)).json()

    def query_people(self, arg):
        """
        Invoques from the API the detail of the proj_id provided to the client
        and returns the context in a JSON file.

        API Calls implemented:

            /people.json will return all people on the account.
            /people/trashed.json will return all people who have been deleted
                from the account. Only admins are able to access trashed people.

        @requires: arg INT type value to signal the index of choice in args
                tuple args = ['people', 'people/trashed']
        @returns: JSON object
        """
        args = ['people', 'people/trashed']
        return self.set_connection('{0}.json'.format(args[arg])).json()

    def detailed_people(self, people_id, arg):
        """
        Invoques from the API the detail of the proj_id provided to the client
        and returns the context in a JSON file.

        API Calls implemented:

            /people/1.json returns the specified person.
            /people/me.json will return the current person but is not in use
                in here because it's the same than the previous one.
            /people/1/projects.json returns a list of all projects the
                specified person has access to, including draft, template,
                archived, and deleted projects. Projects that the requesting
                user does not have access to will not appear in the project
                list. If the requesting user does not have the access rights to
                view the person 404 Not Found will be returned.

        @requires: people_id - INT type value equal to the 'id' identifier
        @requires: arg INT type value to signal the index of choice in args
                tuple args = ['', '/projects']
        @returns: JSON object
        """

        args = ['', '/projects']
        return self.set_connection('people/{0}{1}.json'.format(people_id, args[arg])).json()

    def query_events(self, rv_id, arg, date='', time='', gmt=''):
        """
        Invoques from the API every action registered through the progress log.

        TODO - Polling

        Make sure that you're using the since parameter to limit the result set.
        Use the created_at time of the first item on the list for subsequent
        polls. If there's nothing new since that date, you'll get [] back.

        TODO - Pagination

        We will return 50 events per page. If the result set has 50 entries,
        it's your responsibility to check the next page to see if there are any
        more events -- you do this by adding &page=2 to the query, then &page=3
        and so on.

        API Calls implemented:

            /projects/1/events.json?since=2012-03-24T11:00:00-06:00 returns all
                events in the specified project since 11am CST on March 24, 2012
            /people/1/events.json?since=2012-03-24T11:00:00-06:00 returns all
                the events created by the specified person since 11am CST on
                March 24, 2012.
            /events.json?since=2012-03-24T11:00:00-06:00 returns all events in
                all projects and calendars since 11am CST on March 24, 2012

        @requires: rv_id - identification number of the people or project to
                query about the events related to that people or project.
        @requires: arg INT type value to signal the index of choice in args
                tuple args = ['', 'projects/', 'people/']
        @requires: date - starting date for the query, format: AAAA-MM-DD
        @requires: time - starting time for the query, format: HH:MM:SS
        @requires: gmt - Note that the + character must be url-escaped, while
                the - character can be used as-is. So, use
                ?since=2014-01-01T01:00:00%2B01:00 as opposed to
                ?since=2014-01-01T01:00:00+01:00 for east-of-GMT time zones
        @returns: JSON object
        """
        if arg == 0:
            rv_id += '/'

        args = ['', 'projects/', 'people/']
        return self.set_connection('{0}{1}events.json{2}{3}{4}'.format(args[arg], rv_id, '?since='+date, 'T'+time, gmt)).json()

    def query_todolist(self):
        """
        API Calls implemented:

            /todolists.json shows active to-do lists for all projects.
            /todolists/completed.json shows completed to-do lists for all projects.
            /todolists/trashed.json shows trashed to-do lists for all projects.

            /people/1/assigned_todos.json will return all the to-do lists with to-dos assigned to the specified person.
            /people/1/assigned_todos.json?due_since=2014-07-10 will return all the to-do lists with to-dos assigned to the specified person due after the date specified.

            /projects/1/todos/1.json will return the specified to-do.
            /projects/1/todos/completed.json shows a list of all completed to-dos for this project.
            /projects/1/todos/remaining.json shows a list of all remaining/active to-dos for this project.
            /projects/1/todos.json shows a list of all to-dos for this project; completed and remaining.
            /projects/1/todos.json?due_since=2014-07-10 will return all the to-dos due after the date specified.

            /projects/1/todolists.json shows active to-do lists for this project sorted by position.
            /projects/1/todolists/completed.json shows completed to-do lists for this project.
            /projects/1/todolists/trashed.json shows trashed to-do lists for this project.
            /projects/1/todolists/1/todos.json shows a list of all to-dos for this to-do list; completed and remaining.
            /projects/1/todolists/1/todos/completed.json shows a list of all completed to-dos for this to-do list.
            /projects/1/todolists/1/todos/remaining.json shows a list of all remaining to-dos for this to-do list.
            /projects/1/todolists/1/todos/trashed.json shows a list of all trashed to-dos for this to-do list.
            /projects/1/todolists/1.json will return the specified to-do list including the to-dos.
            /projects/1/todolists/1.json?exclude_todos=true will return the specified to-do list excluding the to-dos. If your to-do lists have a 1000+ total to-dos we request you use the to-do list with the exclude_todos parameter and retrieve to-dos from the to-do endpoints.
        """

        args = ['', 'todolists', 'todolists/completed', 'todolists/trashed',
                'people/', 'projects/', ]
        return self.set_connection(''.format()).json()
