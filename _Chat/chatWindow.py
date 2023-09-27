from tkinter import *
from tkinter import ttk
import tkinter as tk

class AppChat:
	def __init__(self):
		self.root = Tk()
		self.root.title("FTChat")
		self.root.geometry("800x500")
		self.root.resizable(False,False)

		self.widgets()

	def widgets(self):

		self.leftFrame()
		self.centerFrame()
		self.principalEntry = Entry(self.root, width="75").place(x=160, y=460)

	def centerFrame(self):
		self.ce_Frame = Frame(self.root, width="630", height="430").place(x=160,y=10)
		self.vscrollBar = ttk.Scrollbar(self.ce_Frame, orient=tk.VERTICAL)

		self.treeview = ttk.Treeview(self.ce_Frame, yscrollcommand=self.vscrollBar.set)

		self.vscrollBar.config(command=self.treeview.yview)
		self.vscrollBar.place(x=775, y=10, height=430)
		self.treeview.place(x=160,y=10, height="428", width="615")

	def leftFrame(self):
		self.left_Frame = Frame(self.root, width="140", height="477").place(x=10, y=10)

		self.leftTreeview = ttk.Treeview(self.left_Frame)

		item1 = self.leftTreeview.insert('', END, text="Amigos")
		self.leftTreeview.insert(item1, END, text="Amigo 1")
		self.leftTreeview.insert(item1, END, text="Amigo 2")
		self.leftTreeview.insert(item1, END, text="Amigo 3")
		self.leftTreeview.insert(item1, END, text="Amigo 4")

		item2 = self.leftTreeview.insert('', END, text="Juegos")
		self.leftTreeview.insert(item2, END, text="Juego 1")
		self.leftTreeview.insert(item2, END, text="Juego 2")
		self.leftTreeview.insert(item2, END, text="Juego 3")
		self.leftTreeview.insert(item2, END, text="Juego 4")

		self.leftTreeview.place(x=10, y=10, width="140", height="477")
		



