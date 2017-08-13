from zipfile import ZipFile

#This will handle metadata and provide a filetype agnostic way of reading archives
#But right now it's basically just a zipfile wrapper
class SquIFile:
	def __init__(self, file, mode="r",type="z"):
		self._file = ZipFile(file, mode)

	def close(self):
		return self._file.close()

	def open(self, name, mode="r"):
		return self._file.open(name, mode)
