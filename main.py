from tkinter import *
import tkinter as tk
from ventanas.ManuExa import Menu
#from _Chat.chatWindow import AppChat

if __name__ == "__main__":
    ventana = Tk()
    app = Menu(ventana)
    ventana.mainloop()

