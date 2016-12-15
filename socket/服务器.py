##import socket
##
##s = socket.socket()
##
##host = socket.gethostname()
##port = 1234
##s.bind((host, port))
##
##s.listen(5)
##while True:
##    c, addr = s.accept()
##    print 'Got connection from', addr
##    c.send('Thank you for connecting')
##    c.close()

from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'got connection from', addr
        self.wfile.write('Thank you for connecting')

server = TCPServer(('', 1234), Handler)
server.serve_forever()
