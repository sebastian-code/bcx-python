# -*- coding:utf-8 -*-

"""
Created on 2015-04-12
@note: Compatible con Python3
@summary: Cliente para extraccion de informacion de una cuenta de BaseCamp
                   Este cliente unicamente ejecuta accesos de lectura, y esta
                   creado con la finalidad de extraer toda la informacion
                   disponible para la cuenta suministrada, con fines de crear
                   reportes directamente en excel.
@author: Sebastian Reyes Espinosa
@contact: sebaslander@gmail.com
"""

from base64 import b64encode
import sys

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
        self.header_content = {
            'Authorization': self.create_basic_auth(),
            'User-Agent': '{0}:({1})'.format(company, username)
            }

    def create_basic_auth(self):

        """
        Crea un encabezamiento basico de autenticacion para el API
        We don't want to suffer because Python3's strictness about strings
        """

        if sys.version_info >= (3, 0):
            if not isinstance(self.username, str):
                self.username = self.username.decode('utf-8')

            if not isinstance(self.password, str):
                self.password = self.password.decode('utf-8')

            return 'Basic ' + b64encode((self.username + ":" + self.password).encode('utf-8')).decode('utf-8')

        else:
            return 'Basic ' + b64encode(self.username + ":" + self.password).rstrip()

    def _request(self, path, data=None):
        # TODO
        # Crear funcion central para gestion de direccionamiento compatible con
        # API de BaseCamp
        pass

    def test_connection():
        """
        Metodo concebido con la finalidad de validar la conexion a Basecamp
        """
        pass

    def company(self, company_id):
        pass
        """
        Modelo/sugerencia de como definir los metodos de la clase para
        interactuar con el API. En el ejemplo, el metodo busca recuperar la
        informacion de la compañia, si existe

        path = '/contacts/company/%u' % company_id
        return self._request(path)

        """
