from neo4j.v1 import GraphDatabase, basic_auth
import os

class Action(object):

    def __init__(self, id, njuser, njpwd):
        self.id = id
        self.driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth(njuser, njpwd))
        self.session = self.driver.session()

    def track(self):
        raise NotImplementedError("Method must be implemented!")

    def initbatch(self):
        raise NotImplementedError("Method must be implemented!")


class Delete(Action):

    def track(self, ):
        result = self.session.run("MATCH (n:BIBLIOGRAPHICRESOURCE { name: {name} }) REMOVE n:ACTIVE RETURN labels(n)) AS labels", {"name": self.id})
        for recs in result:
            if 'TEMP' in recs['labels']:
                for f in Delete._findfilewithid('/home/seb/temp/test/update/', self.id):
                    os.remove(f)
                for f in Delete._findfilewithid('/home/seb/temp/test/input', self.id):
                    os.remove(f)

        self.session.close()

    @staticmethod
    def _findfilewithid(path, id):
        return [path + f for f in os.listdir(path) if id in f ]



class Create(Action):

    def track(self):
        self.session.run("CREATE (a:BIBLIOGRAPHICRESOURCE:ACTIVE:TEMP { name: {name} })", {"name": self.id})


class Update(Action):

    def track(self):
        pass