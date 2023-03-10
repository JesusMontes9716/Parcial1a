from tkinter import*
from tkinter import ttk

raiz = Tk()

estado = StringVar()
mainFrame = ttk.Frame(raiz, padding="10 10 10 10")#izquierda arriba derecha abajo
mainFrame.grid(column=0, row=0)

frame1 = ttk.Frame(mainFrame, padding="10 10 10 10", borderwidth=3, relief="raised")
frame1.grid(column=0, row=0)

frame2 = ttk.Frame(mainFrame, padding="10 10 10 10", borderwidth=3, relief="raised")
frame2.grid(column=0, row=1)
frame3 = ttk.Frame(mainFrame, padding="10 10 10 10")
frame3.grid(column=1, row=0)
        
nombreEntry = ttk.Entry(frame1, width=30)
nombreEntry.grid(column=1, row=0, pady=12, sticky=(W, E))

aPaternoEntry = ttk.Entry(frame1, width=30)
aPaternoEntry.grid(column=1, row=2, pady=12, sticky=(W, E))

aMaternoEntry = ttk.Entry(frame1, width=30)
aMaternoEntry.grid(column=1, row=3, pady=12, sticky=(W, E))

correoEntry = ttk.Entry(frame1, width=30)
correoEntry.grid(column=1, row=4, pady=12, sticky=(W, E))

movilEntry = ttk.Entry(frame1, width=30)
movilEntry.grid(column=1, row=5, pady=12, sticky=(W, E))
        
ttk.Label(frame1, text="NOMBRE:  ").grid(column=0, row=0, pady=12, sticky=(E))
ttk.Label(frame1, text="AP. PATERNO:  ").grid(column=0, row=2, pady=12, sticky=(E))
ttk.Label(frame1, text="AP. MATERNO:  ").grid(column=0, row=3, pady=12, sticky=(E))
ttk.Label(frame1, text="CORREO:  ").grid(column=0, row=4, pady=12, sticky=(E))
ttk.Label(frame1, text="MOVIL:  ").grid(column=0, row=5, pady=12, sticky=(E))

ttk.Label(frame2, text="Aficiones:  ").grid(column=0, row=0, pady=12, sticky=(E))
leer = ttk.Checkbutton(frame2, text='LEER')
leer.grid(column=0, row=1, sticky=(W))
musica = ttk.Checkbutton(frame2, text='MUSICA')
musica.grid(column=1, row=1, sticky=(W))
videojuegos = ttk.Checkbutton(frame2, text='VIDEOJUEGOS')
videojuegos.grid(column=2, row=1, sticky=(W))

        
comboEstados = ttk.Combobox(mainFrame, textvariable=estado)
comboEstados.grid(column=1, row=1, pady=50)
comboEstados['values']=("Estados 32")
        
ttk.Button(mainFrame, text="GUARDAR",).grid(column=0, row=5, pady=12, sticky=(W))
ttk.Button(mainFrame, text="CANCELAR",).grid(column=0, row=5, pady=12, sticky=(N))

estudiante = ttk.Radiobutton(frame3, text='ESTUDIANTE')
estudiante.grid(column=0, row=0, sticky=(W))
empleado = ttk.Radiobutton(frame3, text='EMPLEADO')
empleado.grid(column=0, row=1, sticky=(W))
desempleado = ttk.Radiobutton(frame3, text='DESEMPLEADO')
desempleado.grid(column=0, row=2, sticky=(W))

nombreEntry.focus()

raiz.mainloop()