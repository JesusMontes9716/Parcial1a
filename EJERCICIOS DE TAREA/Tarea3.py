from tkinter import*
from tkinter import ttk
import tkinter as tk


raiz = Tk()
raiz.config(bg="turquoise4")


imagen1 = PhotoImage(file="1.png")
imagen2 = PhotoImage(file="2.png")
imagen3 = PhotoImage(file="3.png")
imagen4 = PhotoImage(file="4.png")
imagen5 = PhotoImage(file="5.png")

mainFrame = ttk.Frame(raiz, padding="10 10 10 10")#izquierda arriba derecha abajo
mainFrame.grid(column=0, row=1)

frame = Frame(raiz, bg="turquoise4",width=650, height=50)
frame.grid(column=0, row=0)

frame1 = ttk.Frame(mainFrame,  borderwidth=3, relief="raised")
frame1.grid(column=0, row=0)

frame2 = ttk.Frame(mainFrame,  borderwidth=3, relief="raised")
frame2.grid(column=0, row=1)

frame3 = ttk.Frame(mainFrame, padding="5 5 5 5")
frame3.grid(column=1, row=0)
              

etqTexto = Label(frame, bg="turquoise4", fg="white", text="SPAI4.0", font=("Calibri", 35))
etqTexto.grid(column=1, row=0, padx=12)

ttk.Label(frame1, text="LINEA 1:  "   ).grid(column=0, row=0, pady=12, sticky=(E))
ttk.Label(frame1, text="LINEA 2:  ").grid(column=0, row=2, pady=12, sticky=(E))
ttk.Label(frame1, text="LINEA 1:  ").grid(column=0, row=3, pady=12, sticky=(E))
ttk.Label(frame1, text="GABINETE: ABIERTO ").grid(column=0, row=4, pady=12, sticky=(E))
ttk.Label(frame1, text="ALARMA:  ").grid(column=0, row=5, pady=12, sticky=(E))
ttk.Label(frame1, text="ALARMA 2:  ").grid(column=0, row=6, pady=12, sticky=(E))


l1 = ttk.Radiobutton(frame1)
l1.grid(column=1, row=0, sticky=(W))
l2 = ttk.Radiobutton(frame1)
l2.grid(column=1, row=2, sticky=(W))
l11 = ttk.Radiobutton(frame1)
l11.grid(column=1, row=3, sticky=(W))
g = ttk.Radiobutton(frame1)
g.grid(column=1, row=4, sticky=(W))
a = ttk.Radiobutton(frame1)
a.grid(column=1, row=5, sticky=(W))
a2 = ttk.Radiobutton(frame1)
a2.grid(column=1, row=6, sticky=(W))

etqImagen1 =Label(frame, bg="turquoise4")
etqImagen1.grid(column=0, row=0)
etqImagen1['image']= imagen1

etqImagen2 =Label(frame3,bg="black")
etqImagen2.grid(column=0, row=0)
etqImagen2['image']= imagen2

etqImagen3 =Label(frame3)
etqImagen3.grid(column=1, row=0)
etqImagen3['image']= imagen3

etqImagen4 =Label(frame2)
etqImagen4.grid(column=4, row=2)
etqImagen4['image']= imagen4

etqImagen5 =Label(frame2)
etqImagen5.grid(column=6, row=2)
etqImagen5['image']= imagen5



raiz.mainloop()
