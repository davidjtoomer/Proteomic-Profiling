import sys

major = sys.version_info[0]
minor = sys.version_info[1]
if major < 3 or minor < 6:
	print("ERROR: Python version is too old (Python 3.6 required). Update to Python 3.6 or newer.")
	sys.exit(1)

try:
    import pandas
except:
    print("ERROR: Failed to import Pandas.")
    sys.exit(1)

try:
    import selenium
except:
    print("ERROR: Failed to import Selenium.")
    sys.exit(1)

try:
    import bs4
except:
    print("ERROR: Failed to import BeautifulSoup4.")
    sys.exit(1)

try:
    import pyderman
except:
    print("ERROR: Failed to import Pyderman.")
    sys.exit(1)