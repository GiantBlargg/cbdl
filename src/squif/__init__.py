from zipfile import ZipFile
from shutil import copyfileobj

#This will handle metadata and provide a filetype agnostic way of reading archives
#But right now it's basically just a zipfile wrapper
class SquiFile:
	def __init__(self, file, mode="r",type="z"):
		self._file = ZipFile(file+".cbz", mode)

	def close(self):
		return self._file.close()

	def open(self, name, mode="r"):
		return self._file.open(name, mode)

class SquiCol:
	def __init__(self, dest, output):
		pass

	def add(self, file, meta):
		arc = SquiFile(meta["title"], "a")
		destFile = arc.open(meta["name"] + "." + meta["ext"], "w")
		destFile.write(file)
		destFile.close()
