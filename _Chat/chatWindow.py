from tkinter import *

class AppChat:
	def __init__(self):
		self.root = Tk()
		self.root.title("FTChat")
		self.root.geometry("800x500")
		self.root.resizable(False,False)

		self.widgets()

	def widgets(self):
		self.container = Frame(self.root, width="1000", height="600").pack()

		self.left_Frame = Frame(self.container, width="150", height="600", bg="White").place(x=0, y=0)
		self.ce_Frame = Frame(self.container, width="630", height="430", bg="Grey").place(x=160,y=10)
		self.principalEntry = Entry(self.container, width="75").place(x=160, y=460)



