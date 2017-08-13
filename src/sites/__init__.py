import re
import requests

def siteHandle(url, col):
	m=re.match("^(?:(.*):\/\/)?([a-zA-Z0-9-\.]+\.[a-zA-Z0-9-]+)(?:\/(.*))?$", url)
	if m==None :
		print("Invalid URL")
		exit(1)

	if m.group(2) != "dynasty-scans.com":
		print(m.group(2)+" is not supported.")
		exit(1)

	_dynasty(m.group(3), col)

def _dynasty(loc, col):
	loc = loc.split("/")
	if loc[0] != "chapters":
		print(loc[0]+" are unsupported.")
		exit(1)

	_chapter(loc[1], col, {})

def _chapter(name, col, meta):
	r = requests.get("https://dynasty-scans.com/chapters/"+name+".json").json()
	meta["title"] = r["title"]
	for page in r["pages"]:
		meta["name"] = page["name"] + "." + page["url"].split(".").pop()
		print(meta["name"])
		col.add(requests.get("https://dynasty-scans.com"+page["url"]).content, meta)

