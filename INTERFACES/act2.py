from tkinter import *  
from tkinter import ttk

raiz = Tk()
self = Tk

raiz.title("login")
estado = StringVar()
self.usuario='usuario'
self.contraseña='1234'

mainFrame = ttk.Frame(raiz , padding="30 30 40 40")
mainFrame.grid(column=0, row=0)

Frame1 = ttk.Frame(mainFrame,borderwidth=3,relief="raised")
Frame1.grid(column=0,row=0)

Frame2 = ttk.Frame(mainFrame,borderwidth=3,relief="raised")
Frame2.grid(column=2,row=2)

usuarioEntry = ttk.Entry(Frame1, width=30, textvariable=self.usuario)
usuarioEntry.grid(column=1, row=0)

ttk.Label(Frame1, text="NOMBRE").grid(column=0,row=0)
usuarioEntry = ttk.Entry(Frame1, width=30, textvariable=self.usuario)
usuarioEntry.grid(column=1, row=3)
ttk.Label(Frame1, textvariable=self.contraseña).grid(column=1,row=1)

ttk.Label(Frame1, text="AP.PATERNO ").grid(column=0,row=3)
usuarioEntry = ttk.Entry(mainFrame, width=30, textvariable=self.usuario)
ttk.Label(Frame1, textvariable=self.contraseña).grid(column=0,row=4)


ttk.Label(Frame1, text="AP.MATERNO ").grid(column=0,row=5)
usuarioEntry = ttk.Entry(Frame1, width=30, textvariable=self.usuario)
usuarioEntry.grid(column=1, row=5)
ttk.Label(Frame1, textvariable=self.contraseña).grid(column=0,row=6)

ttk.Label(Frame1, text="CORREO ").grid(column=0,row=7)
usuarioEntry = ttk.Entry(Frame1, width=30, textvariable=self.usuario)
usuarioEntry.grid(column=1, row=7)
ttk.Label(Frame1, textvariable=self.contraseña).grid(column=0,row=8)

ttk.Label(Frame1, text="MOVIL ").grid(column=0,row=9)
usuarioEntry = ttk.Entry(Frame1, width=30, textvariable=self.usuario)
usuarioEntry.grid(column=1, row=9)
ttk.Label(Frame1, textvariable=self.contraseña).grid(column=0,row=10)

ttk.Button(mainFrame, text="GUARDAR",command=self.contraseña).grid(column=0,row=20, sticky=(W))
ttk.Button(mainFrame, text="CANCELAR",command=self.contraseña).grid(column=1,row=20, sticky=(W))



comboEstados = ttk.Combobox(raiz, textvariable=estado).grid(column=1,row=20, sticky=(W))
#comboEstados.grid()
#comboEstados['values'] = ('Jalisco', 'Nayarit', 'Colima', 'Michoacan')



chkBoton = ttk.Checkbutton(Frame2, raiz, text="LEER", command= self).grid(column=0,row=0)
chkBoton = ttk.Checkbutton(Frame2,raiz, text="MUSICA", command= self).grid(column=1,row=1)
chkBoton = ttk.Checkbutton(Frame2, raiz, text="VIDEOJUEGOS", command= self).grid(column=2,row=2)


home = ttk.Radiobutton(raiz, text='Estudiante').grid(column=4, row=0, sticky=(W))
home = ttk.Radiobutton(raiz, text='Empleado').grid(column=4, row=1, sticky=(W))
home = ttk.Radiobutton(raiz, text='Desempleado').grid(column=4, row=2, sticky=(W))





raiz.mainloop()