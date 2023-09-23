from tkinter import *
from tkinter import ttk
from ventanas.AppLogin import Login
from ventanas.AppRegistro import Registro

class Menu:
	def __init__(self, ventana):
		self.vent = ventana
		self.vent.title('Menu')
		self.vent.geometry('230x180')
		self.vent.resizable(False, False)

		#Contenedor
		blank = Label(self.vent, text='').pack()
		frame = Label(self.vent, text='¡Bienvenido a la Aplicación!', font=('calibri', 14), fg="Black").pack()
		message = Label(self.vent, text='Elija una Opción', font=('calibri', 14), fg="Black").pack()

		#Botones
		blank = Label(self.vent, text='').pack()
		ttk.Button(self.vent, text='Login', command=self.abrir_login).pack(pady=5)
		ttk.Button(self.vent, text='Registro', command=self.abrir_registro).pack(pady=5)

	def abrir_login(self):
		open_login = Login()
		self.vent.destroy()

	def abrir_registro(self):
		open_registro = Registro()
		self.vent.destroy()