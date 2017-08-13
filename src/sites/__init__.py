import re
import requests

def siteHandle(url, col):
	'''m=re.match("^(?:(.*):\/\/)?([a-zA-Z0-9-\.]+\.[a-zA-Z0-9-]+)(?:\/(.*))?$", url)
	if(m==None):
		print("Invalid URL")
		exit(1)

	if(m.group(2)!="dynasty-scans.com"):
		print(m.group(2)+" is not supported.")
		exit(1)'''

	r = requests.get("http://example.com/")
	col.add(r.content, {"title":"test","name":"example.html"})
