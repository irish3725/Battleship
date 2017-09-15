#!/usr/bin/python3.6

# server from:
# https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/

from http.server import BaseHTTPRequestHandler, HTTPServer

# This class handles requests
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # send response status code
        self.send_response(301) 
        # send headers
        self.send_header('content-type','text/html')
        self.end_headers()

        # send message back to client
        message = "Woah that was a post request."
        # write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    
    # handle get request
    def do_GET(self):
        # send response status code
        self.send_response(200)
        
        # send headers
        self.send_header('content-type','text/html')
        self.end_headers()

        # send message back to client
        message = "Hello world!"
        # write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
    print('starting server...')

    # server setting
    # choosing port 5000 (maybe have to use 5001?)
    server_address = ('127.0.0.1', 5000)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()

