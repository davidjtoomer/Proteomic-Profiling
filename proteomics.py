'''
import pandas as pd
import sys
from bs4 import BeautifulSoup
from tkinter import Tk
from tkinter.filedialog import askopenfilename
'''

from gui.GWindow import GWindow
from gui.GFrame import GFrame

'''
import util
from util.set_driver import *
from util.utils import *


# base URL for the UniProt website, followed by UniProt ID for search result
UNIPROT_URL = 'https://www.uniprot.org/uniprot/'
'''

if __name__ == '__main__':

	# make main window
	root = GWindow()
	root.title("Proteomic Profiling: Subcellular Location Labeler")
	root.mainloop()
	'''
	#######################################################
	# SELECT EXCEL FILE 
	#######################################################

	_ = input("PRESS [ENTER] TO CHOOSE AN EXCEL FILE FOR PROTEOMIC PROFILING.")
	Tk().withdraw() # keep the root window from displaying
	filename = askopenfilename() 

	# make sure that the file is an Excel file
	while not filename.matches('*.xls') or not filename.matches('*.xlsx')
		print("ERROR: File is not a valid Excel sheet.\n")

		_ = input("TYPE \'EXIT\' TO QUIT or PRESS [ENTER] TO CHOOSE AN EXCEL FILE FOR PROTEOMIC PROFILING.")
		if _ == 'EXIT': 
			sys.exit()

		filename = askopenfilename()


	#######################################################
	# GET SHEETS IN EXCEL FILE AND SELECT SHEET(S)  
	#######################################################

	# load the input Excel file
	xls = pd.ExcelFile(filename)
	sheet_names = xls.sheet_names

	# print out all of the sheet names for viewing
	print("SHEET NAMES IN %s:" %filename.upper())
	for i in range(len(sheet_names)):
		print(i + ") " + sheet_names[i])

	# have the user choose which sheet to pick from
	while True:
		sheets = input("CHOOSE ONE OR MORE OF THE ABOVE SHEETS (by NUMBER, comma separated, no spaces after commas): ").replace(" ", "").split(',')
		error = NULL
		if len(sheets) != len(set(sheets)):
			error = "duplicate values"
		for sheet in set(sheets):
			if (!sheet.isdigit() or int(sheet) >= len(sheets)):
				error = "value is not a number or is out of valid range"
		if not error: break
		else: print("ERROR: Input not valid (" + error + ").\n")


	# get columns in sheetname(s)
	# choose column in sheet

	sheet_name = 'Fold 1 over 2+3'
	column_name = 'SECRETED'


	to_label = read_excel_sheet(file_name, sheet_name)
	to_label[column_name] = to_label[column_name].astype('object')

	# install the chromedriver in the util/lib/ directory for scraping the UniProt website
	CHROMEDRIVER_PATH = install_driver()
	driver = setup_driver(CHROMEDRIVER_PATH)

	uniprot_id = to_label['UniprotID']
	for i, ID in uniprot_id.iteritems():
		# replace with progress bar
		if i < 10:
			print("LOOKING AT PROTEIN %d OF %d" %(i, len(to_label)))
			url = UNIPROT_URL + ID
			to_label.at[i, column_name] = extract_data(url, driver) 

	with pd.ExcelWriter(file_name) as writer:
		to_label.to_excel(writer, sheet_name = sheet_name, columns = [column_name])
	'''
	