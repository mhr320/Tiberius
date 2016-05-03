#!/usr/bin/python
from Tkinter import *
import tkMessageBox as mbox
import ttk

"""
Project: Tiberius

Description: GUI for user control of remote monitoring units

"""


class selectables:

    value_of_combo = 'X'

    def __init__(self, parent):
        self.parent = parent
        self.combo()

    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value)
        self.box['values'] = ('Command #1', 'Command #2', 'Command #3')
        self.box.current(0)
        self.box.grid(column=0, row=0, sticky=W)

class Tiberius(Frame):

	def __init__(self, parent):
		# inherit from the Frame container widget
		Frame.__init__(self, parent)
		# save a reference to the parent widget; in this case, parent widget is Tk root window
		self.parent = parent
		# use initUserInterface method to create the user interface
		self.initUserInterface()
				
	def initUserInterface(self):
		# set title of window
		self.parent.title("Tiberius User Interface")
		# use pack geometry manager to place the Frame widget, 
		# expand in both directions to take the whole space of the root window
		self.grid()
		# create button widget; link button click to command to execute
		statusButton = Button(self, text="Status Check", command=self.onStatusButton)
		# place 5 pixels of padding around button in x and y directions
		statusButton.grid(column=2, row=2)

		downloadFileButton = Button(self, text="Download File")
		downloadFileButton.grid(column=3, row=3)

		sendCommandButton = Button(self, text="Send Command")
		sendCommandButton.grid(column=10, row=0, sticky=E)

	def onStatusButton(self):
		# if status button pressed, show dialog box
		mbox.showinfo("Info", "Checking Status")
		
def main():
	# create root window
	root = Tk()
	root.columnconfigure(0, weight=2)
	root.rowconfigure(0, weight=2)
	# creates selectables class instance
	app = selectables(root)
	# create an instance of our application class
	app = Tiberius(root)
	"""
	mac OS needs 
		root.lift()
		root.attributes('-topmost',True)
		root.after_idle(root.attributes,'-topmost',False) 
	at least before bundling into a full app. In order 
	to *start* application window on top of all others
	please test for Windwos OS

	"""
	root.lift()
	root.attributes('-topmost',True)
	root.after_idle(root.attributes,'-topmost',False)
	# start event handling by entering mainloop
	# mainloop receives events from the windows system and dispatches to application widgets
	root.mainloop()
		
if __name__ == '__main__':
	main()