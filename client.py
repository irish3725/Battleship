#!/usr/bin/python3.6

import re
import sys
import argparse
import http.client, urllib.parse

def run():

    ip = sys.argv[1]
    port = sys.argv[2]
    x = int(sys.argv[3])
    y = int(sys.argv[4])
    host = ip + ':' + port

    # parameters for the request request
    params = urllib.parse.urlencode({'x': x, 'y': y})
    print(params)   
    # headers for post request
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    # connection to server
    conn = http.client.HTTPConnection(host)
    # make a post request
    conn.request("POST", "/", params, headers)
    # get the response to that request and save it to r1
    r1 = conn.getresponse()
    # print the contents(html code) of that response
    print(r1.read())
    print(r1.status,r1.reason)
    conn.close()
    updateBoard(r1.reason,params)

def updateBoard(message,params):
    # get hit/sink results
    result = re.match('(hit=)(\d)(sink=)(\w*)(.*)',message)
    if result == None: 
        print("result was none")
        return
    hit = result.group(2)
    sink = result.group(4)
    
    # if hit is true make that on opponent board.
    opponent = open('opponent.txt', 'r')
    oBoard = opponent.read()
    opponent.close()
    x = int(float(params[2]))
    y = int(float(params[6]))
    index = x + (11 * y)
    mark = "-"
    if hit == "1":
        mark = "x"
    if sink != "":
        mark = sink
    print('x =',x) 
    print('y =',y) 
    oBoard = oBoard[:index] + mark + oBoard[index+1:]
    print(oBoard)
    opponent = open('opponent.txt', 'w')
    opponent.write(oBoard)
    opponent.close() 
    print('hit =',hit)
    print('sink =',sink)

run()

