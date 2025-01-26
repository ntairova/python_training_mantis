from datetime import datetime


class Project:

    def __init__(self, project):
        self.project = project

    def __repr__(self):
        return "%s" % self.project





    #def __eq__(self, other):
       # return (self.id is None or other.id is None or self.id == other.id and self.name == other.name)

