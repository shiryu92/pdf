'''
	Author: shiryu92
	Module: Parse pdf file 
	Date: 30/07/2015
'''

import os 
import mmap
import map
import pdfparser



def main():
	pdf_map 	= map.MFile('sample.pdf')
	mpdf 		= pdf_map.mapfile()
	
	
	pdf_parser 	= pdfparser.PDFParser(mpdf)
	pdf_parser.is_pdf()
	print pdf_parser.get_version()
	
	pdf_map.unmap()
	
	
if __name__ == "__main__":
	main()
