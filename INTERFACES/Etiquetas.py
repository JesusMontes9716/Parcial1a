from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Label(raiz, text= "ETIQUETA SOLO TEXTO")
etqTexto.grid()

imagen = PhotoImage(file= "imagen.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen 

etqCombinada = ttk.Label(raiz, text="etqCombinada" , compound="center")
etqCombinada.grid()
etqCombinada['image'] = imagen

raiz.mainloop()