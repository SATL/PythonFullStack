from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import hello_api
from api.restaurantApi import RestaurantApi

basicApi = hello_api.helloApi()
restaurantApi = RestaurantApi()
class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if( self.path.endswith("/hello") ):
                basicApi.helloGet(self);
            if( self.path.endswith("/hola") ):
                basicApi.helloGet(self);
            if( self.path.endswith("/restaurant") ):
                restaurantApi.getAll(self)


        except IOError:
            server.send_error(404, 'File Not Found: %s' % server.path)


    def do_POST(self):
        if( self.path.endswith("/hello") ):
            basicApi.helloPost(self)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()