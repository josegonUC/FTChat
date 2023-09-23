from tkinter import *
import tkinter as tk
from _Chat.chatWindow import Appchat

class Login:
	def __init__(self):
		self.vent = Tk()
		self.vent.geometry('250x250')
		self.vent.title('Login')
		self.vent.resizable(False, False)

		self.nombre = StringVar()
		self.contraseña = StringVar()

		self.widgets()

	def widgets(self):

		blank =Label(self.vent, text='').pack()
		frame = Label(self.vent, text='Intruduzca sus Datos', font=('calibri', 14), fg='Black').pack()

		#inputs
		self.username_label = Label(self.vent, text='Nombre:', font=('calibri', 12), fg='Black').place(x=5, y=70)
		self.username_input = Entry(self.vent, textvariable=self.nombre).place(x=70, y=69)

		self.password_label = Label(self.vent, text='Contraseña:', font=('calibri', 12), fg='Black').place(x=5, y=105)
		self.password_input = Entry(self.vent, textvariable=self.contraseña).place(x=90, y=104)

		#Botones
		self.boton1 = Button(self.vent, text='Login', font=('calibri', 12), command=self.abrir_chat).place(x=90, y= 170)

	def abrir_chat(self):
		open_chat = Appchat()
		self.vent.destoy()
