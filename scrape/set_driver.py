import pyderman as driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def install_driver():
	"""
	This method installs a chrome driver in the /src/lib directory to
	allow for websraping through Google Chrome. It returns the path to
	the chromedriver.
	"""

	PATH = driver.install(browser = driver.chrome)
	print("INSTALLED CHROMEDRIVER AT PATH: %s" %PATH)
	return PATH

def setup_driver(path):
	"""
	This method configures the webdriver. It adds the headless feature, 
	which allows requests to be pulled from the browser without seeing 
	the browser pop up every time. It returns the fully configured 
	chromedriver.
	"""

	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome(path, options = options)
	return driver