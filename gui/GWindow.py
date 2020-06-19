import tkinter as tk
import tkinter.font as font
from gui.GFrame import GFrame, GSeparator
from gui.Meta import *

class GWindow(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		# set window size, move to center of the screen 
		self.update_idletasks()
		xpos = (self.winfo_screenwidth() // 2) - (window_width // 2)
		ypos = (self.winfo_screenheight() // 2) - (window_height // 2)
		self.geometry('{}x{}+{}+{}'.format(window_width, window_height, xpos, ypos))

		# expand all frames to fit full column width
		self.columnconfigure(0, weight = 1)

		# set background color
		self.configure(bg = bg1, padx = 10, pady = 10)

		# begin the program
		self.introduction()

		# fonts = font.families()
		# for ex in fonts:
			# print(ex + '\n')

	def introduction(self):

		header_frame = GFrame(self)
		header_frame.grid(row = 0, column = 0, sticky = 'WE')

		# header label
		header = tk.Label(header_frame, text = introduction_header_text, bg = bg2, fg = accent1)
		header['font'] = font.Font(family = family, size = h3, weight = font.BOLD)
		header.grid(row = 0, column = 0)
		
		self.separate() # note: uses row 1

		# introduction frame
		introduction_frame = GFrame(self)
		introduction_frame.grid(row = 2, sticky = 'WE')

		introduction = tk.Message(introduction_frame, text = introduction_text, bg = bg2, fg = fg, anchor = 'w', justify = tk.LEFT, width = window_width - 50)
		introduction['font'] = font.Font(family = family, size = p)
		introduction.grid(row = 0, column = 0, sticky = 'WE')

		# add button to move to the next section
		advance = tk.Button(introduction_frame, text = 'Click Here to Continue', fg = bg1, padx = 20, pady = 10)
		advance.grid(row = 1, column = 0)

	def separate(self):
		separator = GSeparator(self, height = 10)
		separator.grid()

	def choose_file(self):
		return


















