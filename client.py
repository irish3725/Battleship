#!/usr/bin/python3.6

import http.client, urllib.parse

# parameters for the request request
params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
# headers for post request
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
# connection to server
conn = http.client.HTTPConnection("bugs.python.org")
# make a post request
conn.request("POST", "", params, headers)
# get the response to that request and save it to r1
r1 = conn.getresponse()
# print the contents(html code) of that response
print(r1.read())

