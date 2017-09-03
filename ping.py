#!/usr/bin/python3
import sys
import requests
from requests import Request
import webbrowser
import os
import time

#dont forget alias ping="./ping.py" or alias ping="python3 ping.py"
ping_command = "/bin/ping -O"
success_ping_command = "/bin/ping -O -c1"
fake_address = "1.1.1.1"
ok_address = "8.8.8.8"
google_search = "https://www.google.com/search"

def sed_command(address, request):
	return "sed 's/%s/\"%s\"/g'" % (address, request)
	
request = sys.argv[1]

r = requests.get(google_search, params={"q": request})
response = r.text

if ('class="spell' in response): #quick and dirty, but works
	os.system("%s %s | %s" % (ping_command, fake_address, sed_command(fake_address, request)))
else:
	os.system("%s %s | %s" % (success_ping_command, ok_address, sed_command(ok_address, request)))
	print("Ok")
	time.sleep(2)
	#better parse the answer for first url, but screw that
	url_request = Request('GET', google_search, params={"q": request, "btnI": ""}).prepare()

	webbrowser.open(url_request.url)

