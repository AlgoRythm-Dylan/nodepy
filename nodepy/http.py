"""

https://nodejs.org/api/http.html

"""

from .net import net

class http:

    class Server(net.Server):

        def __init__(self):
            # Set default values
            self.port = 8080
            self.listening = False
            self.maxHeadersCount = 2000 # TODO: Implement
            self.timeout = 120 # TODO: Implement
            self.keepAliveTimeout = 5 # TODO: Implement

        def listen(self, port):
            self.port = port
            self.listening = True

    def create_server(requestListener=None, options={}):
        print("Isn't that just fine?")