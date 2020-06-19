'''
Contains the metavariables for all of the graphics displays,
as well as any long text strings.
'''

# font family and sizing
family = 'DIN Alternate'
h1 = 36
h2 = 30
h3 = 24
h4 = 18
p = 14

# color scheme
fg = '#f0f0f0' 
bg1 = '#121521'
bg2 =  '#23273b'
accent1 = 'light sky blue'

# window specs
window_width = 1000
window_height = 600

# text for the introduction screen
introduction_header_text = "PROTEOMIC PROFILE: Subcellular Location Annotator"

introduction_text = (
	'Welcome to the Subcellular Location Annotator! This application will help you '
	'retrieve the subcellular location of any protein for which you have the UniProt ID. '
	'The program scrapes the UniProt website in real time, so any updates to the website '
	'are automatically accounted for in the program (i.e. you don\'t need to update the program '
	'or re-download any information from the website. If for any reason you find any issues, '
	'or if you want there to be more options in the program, feel free to contact David Toomer at '
	'djtoomer@stanford.edu with a specific request, and he will promptly work to fix the app. The source '
	'code for the app is also hosted at https://www.github.com/davidjtoomer/Proteomic-Profiling. \n\n'
	'You will need to have all of the valid UniProt IDs of the proteins you want listed in a column '
	'or columns in an Excel spreadsheet in order for the program to work. You will enter those '
	'column(s) on the next page, and the program will get to work! \n'
)