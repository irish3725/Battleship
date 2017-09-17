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
    #params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
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
    updateBoard(r1.reason)

def updateBoard(message):
    result = re.match('(hit=)(\d)(sink=)(\d)',message)
    hit = result.group(2)
    sink = result.group(4)
    print('hit =',hit)
    print('sink =',sink)

run()

