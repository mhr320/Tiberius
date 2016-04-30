#!/usr/bin/python

from Tkinter import *
import tkMessageBox as mbox

"""
Project: Tiberius

Description: GUI for user control of remote monitoring units

"""

width = 250
height = 150

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
		# use pack geometry manager to place the Frame widget, expand in both directions to take the whole space of the root window
		self.pack(fill=BOTH, expand=True)
		# create button widget; link button click to command to execute
		statusButton = Button(self, text="Status Check", command=self.onStatusButton)
		# place 5 pixels of padding around button in x and y directions
		statusButton.pack(padx=5, pady=5)
		
		downloadFileButton = Button(self, text="Download File")
		downloadFileButton.pack(padx=5, pady=5)
		
	def onStatusButton(self):
		# if status button pressed, show dialog box
		mbox.showinfo("Info", "Checking Status")
		
def main():
	# create root window
	root = Tk()
	# set size of window (width height xScreen yScreen)
	root.geometry("500x300+300+300")
	# create an instance of our application class
	app = Tiberius(root)
	# start event handling by entering mainloop
	# mainloop receives events from the windows system and dispatches to application widgets
	root.mainloop()
		
		
if __name__ == '__main__':
	main()