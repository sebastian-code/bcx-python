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
            dashboard and reporting tool, because basecamp has none.
@author: Sebastian Reyes Espinosa
@contact: sebaslander@gmail.com
"""

import requests

__author__ = 'Sebastian Reyes Espinosa'
__email__ = 'sebaslander@gmail.com'
__creation_date__ = '2015-04-12'


class Basecamp():

    def __init__(self, user_id, username, password, company):
        # Definir caracteristicas del objeto de conexion
        self.base_url = 'https://basecamp.com/%s/api/v1/' % user_id
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

    def query_projects(self):
        """
        Invoques from the API a list of all active projects into the platform
        and returns the context in a JSON file.

        API Calls implemented:

            /projects.json

        """

        r = self.set_connection('projects.json')
        return r.json()

        # li = [u['id'] for u in list_data]
        # detail_data = self.detailed_projects(li[0])
        # detail_data = [self.detailed_projects(x) for x in li]
        # return list_data, detail_data

    def detailed_projects(self, proj_id):
        # /projects/1.json returns a detailed report of the specified project
        # where 1 equals to the id of the project.

        return self.set_connection('projects/{0}.json'.format('proj_id'))

    """
    #TODO
    From projects listing still is pending to implement this API calls:

    /projects/drafts.json returns all draft projects.
    /projects/archived.json returns all archived projects.

    API calls functionalities still pending to include:

    Project Templates
    Stars
    People
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
    """
