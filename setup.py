from setuptools import setuptools

APP = ['proteomics.py']
APP_NAME = "Proteomic Profile"
DATA_FILES = ['data/secreted.xlsx', 'data/random.xlsx']

OPTIONS = {
	'argv_emulation': True,
	'iconfile': 'icon/icon.icns',
	'plist': {
		'CFBundleName': APP_NAME,
		'CFBundleDisplayName': APP_NAME,
		'CFBundleVersion': '0.1.0',
		'CFBundleShortVersionString': '0.1.0',
		'NSHumanReadableCopyright': 'Copyright © 2020, David Toomer, All Rights Reserved'
	}
}

setup(
	name = APP_NAME,
	app = APP,
	data_files = DATA_FILES,
	options = {'py2app': OPTIONS},
	setup_requires = ['py2app']
)