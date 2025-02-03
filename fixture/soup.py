
from suds import *
from suds.client import Client


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
        try:
            res = client.service.mc_projects_get_user_accessible(username, password)
            names = []
            for i in range(len(res)):
                name = getattr(res[i], "name")
                names.append(name)
            return names
        except WebFault:
            return False









