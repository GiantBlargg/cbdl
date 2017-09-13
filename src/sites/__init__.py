import re
import requests

handlers = []


def siteHandle(url, col):
	for h in handlers:
		if h(url, col):
			return True
	return False


def simpleDownload(url):
	return lambda: requests.get(url).content


def include(regexString):
	regex = re.compile(regexString)

	def append(f):

		def wrap(url, col):
			m = regex.match(url)
			if m == None:
				return False
			f(url, m, col)
			return True

		handlers.append(wrap)
		return f

	return append


import sites.dynasty
