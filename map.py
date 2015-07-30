'''
	Author: shiryu92
	Module: Map file to memory
	Date: 30/07/2015
'''

import mmap

class MFile:
	''' Map file to memory '''
	
	def __init__(self, filepath);
		''' Init file path '''
		self.filepath = filepath
		self.file     = None 
		self.map 	  = None
	
	def mapfile(self):
		''' Map file '''
		try:
			file = open(self.filepath)
			map  = mmap.mmap(file.fileno(), 0, access = mmap.ACCESS_READ)
			return map
		except Exception:
			return None 
	
	def unmap(self):
		''' Unmap file '''
		if self.map  != None:
			self.map.close()
			
		if self.file != None:
			self.file.close()
		