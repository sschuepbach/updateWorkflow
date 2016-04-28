from enum import Enum

from py2neo import Graph

from ingest import actions

Actions = Enum(CREATE='CREATE', DELETE='DELETE', UPDATE='UPDATE')


class Message(object):
    action = str
    graph = Graph()

    def __init__(self, msgname: str):
        splittedmsg = msgname.split('#')
        if splittedmsg[2] == Actions.CREATE:
            action = actions.Create
        elif splittedmsg[2] == Actions.DELETE:
            action = actions.Delete
        elif splittedmsg[2] == Actions.UPDATE:
            action = actions.Update
        else:
            raise ValueError('Action {}'.format(splittedmsg[2]))
        action.track()
        action.initbatch()
