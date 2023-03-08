from tkinter import *  
from tkinter import ttk

class act1: 
    #tipo de constructor
    def _init_(self, raiz):
      raiz.title("INICIO DE SECION")

      self.usuario='USUARIO '
      self.contraseña='1234'
     
      mainFrame = ttk.Frame(raiz , padding="3 3 12 12")
      mainFrame.grid(column=0, row=0)
      usuarioEntry = ttk.Entry(mainFrame, width=30, textvariable=self.usuario)
      usuarioEntry.grid(column=1, row=0)

      ttk.Label(mainFrame, text="Usuario").grid(column=0,row=0)
      usuarioEntry = ttk.Entry(mainFrame, width=30, textvariable=self.usuario)
      usuarioEntry.grid(column=1, row=3)
      ttk.Label(mainFrame, textvariable=self.contraseña).grid(column=1,row=1)
      ttk.Label(mainFrame, text="Contraseña ").grid(column=0,row=3)
      ttk.Label(mainFrame).grid(column=0,row=4)
      ttk.Button(mainFrame, text="Ingresar",command=self.contraseña).grid(column=1,row=5,sticky=(E))

if __name__=="__main__":
  print("Este es el archivo Principal.")
  print("Nada mas se mostrara esto si es el Pricipal")
