from tkinter import *
import tkinter as tk
from ventanas.AppLogin import Login
import sqlite3 as sql

class Registro(Login):
	def __init__(self):
		
		Login.__init__(self)
	
		self.boton2 = Button(self.vent, text='Registrar', font=('calibri', 12), command=self.accion_registrar).place(x=80, y= 205)

	def accion_registrar(self):

		nombre = self.nombre.get() 
		psword = self.contraseña.get()

		conn = sql.connect("database.db")
		cursor = conn.cursor()

		cursor.execute("INSERT INTO usuarios (NOMBRE,PASS) VALUES ('"+nombre+"', '"+psword+"');")

		if cursor.fetchall():
			self.message = Label(self.vent, text='¡Registrado con Exito!', font=('calibri', 14),fg='Red').place(x=55, y=140)
			conn.commit()
		else:
			self.message2 = Label(self.vent, text='¡Registro Fallido!', font=('calibri', 13), fg='Red').place(x=60, y=140)
		
		conn.close()


		