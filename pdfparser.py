'''
	Author: shiryu92
	Module: pdf parser 
	Date: 30/07/2015
'''

class PDFParser:
	''' PDF parser class '''
	def __init__(self, mpdf):
		''' Init '''
		self.mpdf = mpdf
	
	
	def is_pdf(self):
		''' Check the file is pdf '''
		self.pdf_sig 		= self.mpdf[:5]
		self.pdf_version 	= None
		
		if self.pdf_sig == "%PDF-":
			self.pdf_version = self.mpdf[5:8]
			return True
		else:
			return False
		
	def get_version(self):
		''' Get pdf version '''
		return self.pdf_version
	