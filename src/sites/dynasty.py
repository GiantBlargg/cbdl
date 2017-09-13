import requests
import sites


@sites.include(
	"^(?:(?:https?)?://)?dynasty-scans\.com/(chapters|series|anthologies)/([a-z1-9_]+)$"
)
def dynasty(url, m, col):
	type = m.group(1)
	name = m.group(2)
	if type == "chapters":
		return _chapter(name, col, {})

	if type == "series" or loc[0] == "anthologies":
		return _series(type, name, col, {})

	exit(1)


def _chapter(name, col, meta):
	r = requests.get("https://dynasty-scans.com/chapters/" + name + ".json").json()
	meta["title"] = r["title"]
	for tag in r["tags"]:
		if tag["type"] == "Series":
			meta["series"] = tag["name"]
	for page in r["pages"]:
		meta["name"] = page["name"]
		meta["ext"] = page["url"].split(".").pop()
		print(meta["name"])
		col.add(sites.simpleDownload("https://dynasty-scans.com" + page["url"]), meta)


def _series(type, name, col, meta):
	r = requests.get("https://dynasty-scans.com/" + type + "/" + name + ".json").json()#yapf:disable
	for i in r["taggings"]:
		if "header" in i:
			meta["volume"] = i["header"]
			print(meta["volume"])
		else:
			print(i["title"])
			_chapter(i["permalink"], col, meta)
