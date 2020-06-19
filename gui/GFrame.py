import tkinter as tk
from gui.Meta import *

class GFrame(tk.Frame):

	def __init__(self, master = None, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)

		self.master = master
		self.configure(bg = bg2, padx = 10, pady = 8)


class GSeparator(tk.Frame):

	def __init__(self, master = None, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)

		self.master = master
		self.configure(bg = bg1)