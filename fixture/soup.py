import json
from http.client import responses

from suds.client import Client
from suds import WebFault
from suds import *
from suds import sudsobject
import json
from suds.sudsobject import asdict, recursive_asdict


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
           client.service.mc_login(username, password)
           return True
        except WebFault:
            return False

    def list_of_projects(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        response = client.service.mc_projects_get_user_accessible(username, password)
        result = []
        for res in range(len(response)):
            res = json.dumps(recursive_asdict(response))
            result.append(res)
        return result









