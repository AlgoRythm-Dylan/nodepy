"""

https://nodejs.org/api/net.html

"""

from .events import events

class net:

    class Server(events.EventEmitter):

        def __init__(self, options=None, connection_listener=None):
            if(connection_listener == None):
                connection_listener = options
            if(connection_listener != None):
                self.on("connection", connection_listener)


        def listen(self, port, host="localhost"):
            pass

    def create_server(options=None, connection_listener=None):
        if(connection_listener == None):
            connection_listener = options # NodeJS does this swap

    def _default_socket_listeners():
        return {
            "close": [],
            "connect": [],
            "data": [],
            "drain": [],
            "end": [],
            "error": [],
            "lookup": [],
            "ready": [],
            "timeout": []
        }

    class Socket(events.EventEmitter):

        def __init__():
            self.listeners = _default_socket_listeners()