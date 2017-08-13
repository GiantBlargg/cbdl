def siteHandle(url):
	m=re.match("^(?:(.*):\/\/)?([a-zA-Z0-9-\.]+\.[a-zA-Z0-9-]+)(?:\/(.*))?$", url)
	if(m==None):
		print("Invalid URL")
		exit(1)

	if(m.group(2)!="dynasty-scans.com"):
		print(m.group(2)+" is not supported.")
		exit(1)
