from zipfile import ZipFile
from shutil import copyfileobj
import os
import pystache


#This will handle metadata and provide a filetype agnostic way of reading archives
#But right now it's basically just a zipfile wrapper
class SquiFile:

	def __init__(self, file, mode="r", type="z"):
		self._file = ZipFile(file + ".cbz", mode)

	def close(self):
		return self._file.close()

	def open(self, name, mode="r"):
		return self._file.open(name, mode)


class SquiCol:

	def __init__(self, dest, output):
		self._dest = dest
		self._output = output
		self._arcName = None
		self._arcFile = None

	def add(self, file, meta):
		arcname, filename = self._genArcName(meta)
		if arcname != self._arcName:
			if self._arcFile != None:
				self._arcFile.close()

			os.makedirs(os.path.dirname(arcname), exist_ok=True)
			self._arcFile = SquiFile(arcname, "a")

		destFile = self._arcFile.open(meta["name"] + "." + meta["ext"], "w")
		destFile.write(file())

	def close(self):
		self._arcFile.close()
		self._arcName = None
		self._arcFile = None

	def _genArcName(self, meta):
		out = pystache.render(self._output, meta).split(";", 1)
		out[1] = "/".join(out[1].split(";"))
		return self._dest + "/" + out[0], out[1]
