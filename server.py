#!/usr/bin/python3.6

# server from:
# https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/

import argparse
import sys
import cgi 
import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer

# This class handles requests
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        
        # make sure request is formatted correctly
        try:
            ctype, pdict = cgi.parse_header(self.headers['content-type'])
        # if not, send error 400 
        except TypeError:
            self.send_error(400, 'not formatted correctly')
        
        length = int(self.headers['content-length'])
        postvars = urllib.parse.parse_qs(self.rfile.read(length), keep_blank_values=1)
        
        for key in postvars:
            if str(key) == "b'x'":
                x = postvars[key]
            elif str(key) == "b'y'":
                y = postvars[key]
       
        # change values from lists to integers
        x = int(x[0])
        y = int(y[0])
       
        # check to see if values are in bounds 
        if x > 9 or x < 0 or y > 9 or y < 0:
            #self.send_response(404)
            #self.send_header('content-type','text/html')
            #self.end_headers()
            self.send_error(404, 'out of bounds') 
            return
       
        # if they are in bounds 
        index = (11*y) + x
        print(x, y, index)
        hit = checkBoard(index)
        if hit == 0:
            hit = 0
        elif hit == 1:
            self.send_error(410, 'alrady fired there')
            return
        elif hit == 2:
            hit = 1
        message = 'hit=%d' % hit
        message = message + 'sink=0'
        print(message)

        headers = {"Content-type": "applicaton/x-www-form-urlencoded", "Accept": "text/plain"}

        # send response status code
        self.send_response(200,message) 
        # send headers
        self.send_header('content-type','text/html')
        self.end_headers()

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

def checkBoard(i):
    print(board[i])
    if board[i] == '_':
        return 0 
    elif board[1] == '-' or board[1] == 'x':
        return 1 
    else:
        return 2

def readBoard(f):
    b = ""
    with open(f, 'r') as infile:
        for line in infile:
            b = b + line
    global board
    board = b
    return b

def run():
    
    port = int(sys.argv[1])
    f = sys.argv[2]
    readBoard(f)
    print(board)
    print('starting server...')
    # server setting
    # choosing port 5000 (maybe have to use 5001?)
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()

