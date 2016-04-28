import selectors
import socket
import configparser

__author__ = "Sebastian Schüpbach"
__copyright__ = "Copyright 2016, swissbib project, UB Basel"
__license__ = "http://opensource.org/licenses/gpl-2.0.php"
__version__ = "0.1"
__maintainer__ = "Sebastian Schüpbach"
__email__ = "sebastian.schuepbach@unibas.ch"
__status__ = "development"

"""
main.py serves as the entry point for processing incoming CBS messages. Depending on the 'action' defined in the
filename (CREATE, UPDATE, DELETE) a processing workflow is initialized. Furthermore it listens to socket messages from
the updateWrapper and suspends or continues.
"""

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()
    print('acceted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1000)
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


config = configparser.ConfigParser()
config.read('config.ini')

sock = socket.socket()
sock.bind((config['SOCKET']['host'], int(config['SOCKET']['port'])))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
