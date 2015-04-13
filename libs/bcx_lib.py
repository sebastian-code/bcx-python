# -*- coding:utf-8 -*-

"""
Created on 2015-04-12
@note: Compatible con Python3
@summary: Cliente para extraccion de informacion de una cuenta de BaseCamp
                   Este cliente unicamente ejecuta accesos de lectura, y esta
                   creado con la finalidad de extraer toda la informacion
                   disponible para la cuenta suministrada, con fines de crear
                   reportes directamente en excel.
@disclaimer: Este cliente trabaja con autenticacion basica http, por lo que solo
                    es recomendado para uso personal, bajo condiciones de
                    control del ambiente de trabajo, donde no haya riesgo a
                    perdidas de informacion.
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
            print('Error de conexion', e)

    def projects_list(self):
        """
        Devuelve una lista de todos los proyectos activos
        """
        path = 'projects.json'
        return self.set_connection(path)
