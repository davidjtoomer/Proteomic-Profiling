import pandas as pd
import openpyxl
from bs4 import BeautifulSoup
from set_driver import *
# from gwindow import *

UNIPROT_URL = 'https://www.uniprot.org/uniprot/'

def read_excel_sheet(filename, sheetname):
	xls = pd.ExcelFile(filename)
	sheet = pd.read_excel(filename, sheetname)
	return sheet

def extract_data(url, driver):
	"""
	This function retrieves the proper UniProt annotation from the UniProt website.
	It returns the proper string to fit into the excel sheet by dividing into three
	categories:
		1. No UniProt annotation: returns '?'
		2. UniProt annotation without secreted/extracellular: 'n'
		3. UniProt annotation with secreted/extracellular: 'secreted' or the direct text from the annotation
	"""

	# digest the HTML from the UniProt database
	driver.get(url)
	content = driver.page_source
	soup = BeautifulSoup(content, features = 'html.parser')

	# if there is not an annotation, fill the sheet with '?'
	annotation = soup.find('div', attrs = {'class': 'tabsContent', 'id': 'table-uniprot_annotation'})
	if not annotation: return '?'

	# if there is an annotation, but no extracellular/secreted component, fill the sheet with 'n'
	extracell = annotation.find('li', attrs = {'class': 'Extracellular_region_or_secreted'})
	if not extracell: return 'n'

	# fill the spreadsheet with the annotation
	subcell_loc = extracell.find('a', href = True)
	data = subcell_loc.text.strip().lower()
	return 'secreted' if 'secreted' in data else data


if __name__ == '__main__':
	CHROMEDRIVER_PATH = install_driver()
	driver = setup_driver(CHROMEDRIVER_PATH)

	file_name = '../../test_uniprot.xlsx'
	sheet_name = 'Fold 1 over 2+3'
	column_name = 'SECRETED'

	wb = openpyxl.load_workbook(file_name)
	sheet = wb.get_sheet_by_name(sheet_name)


	to_label = read_excel_sheet(file_name, sheet_name)
	to_label[column_name] = to_label[column_name].astype('object')
	

	uniprot_id = to_label['UniprotID']
	for i, ID in uniprot_id.iteritems():
		if i < 10:
			print("LOOKING AT PROTEIN %d OF %d" %(i, len(to_label)))
			url = UNIPROT_URL + ID
			to_label.at[i, column_name] = extract_data(url, driver) 

	with pd.ExcelWriter(file_name) as writer:
		to_label.to_excel(writer, sheet_name = sheet_name, columns = [column_name])
	