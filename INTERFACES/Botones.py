from tkinter import *
from tkinter import ttk

raiz =  Tk()
boton = ttk.Button(raiz, text="BOTON SOLO TEXTO")
boton.grid()

imagen = PhotoImage(file="imagen2.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image'] = imagen

btnCombinada = ttk.Button(raiz, text="BOTON COMBINADO", compound="bottom")
btnCombinada.grid()
btnCombinada['image'] = imagen

chkBoton = ttk.Checkbutton(raiz, text="Opcion 1")
chkBoton.grid()

raiz.mainloop()
