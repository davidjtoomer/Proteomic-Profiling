import pandas as pd



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