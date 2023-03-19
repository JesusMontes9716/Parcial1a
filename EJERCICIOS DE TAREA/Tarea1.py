from tkinter import*
from tkinter import ttk

raiz = Tk()
raiz.geometry("600x450")
notebook = ttk.Notebook(raiz)
notebook.pack()

s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="blue")
s.map("TNotebook", background= [("selected", "blue")])

frame1 = ttk.Frame(notebook, width=500, height=500)
frame1.pack(fill='both', expand='1')
frame2 = ttk.Frame(notebook, width=500, height=500)
frame2.pack(fill='both', expand='1')
frame3 = ttk.Frame(notebook, width=500, height=500)
frame3.pack(fill='both', expand='1')
frame4 = ttk.Frame(notebook, width=500, height=500)
frame4.pack(fill='both', expand='1')
frame5 = ttk.Frame(notebook, width=500, height=500)
frame5.pack(fill='both', expand='1')

notebook.add(frame1, text="          ADD          " )
notebook.add(frame2, text="           DELETE          ")
notebook.add(frame3, text="           SEARCH         ")
notebook.add(frame4, text="           SERVICES          ")
notebook.add(frame5, text="           HELP          ")

frame6 = ttk.Frame(frame1, padding="150 5 251 5", borderwidth=3, relief="raised")#izquierda arriba derecha abajo
frame6.grid(column=0, row=0)

frame7 = ttk.Frame(frame1, padding="33 10 132 10", borderwidth=3, relief="raised")#izquierda arriba derecha abajo
frame7.grid(column=0, row=1)

frame8 = ttk.Frame(frame1, padding="12 10 148 10", borderwidth=3, relief="raised")#izquierda arriba derecha abajo
frame8.grid(column=0, row=2)

frame9 = ttk.Frame(frame1, padding="20 10 136 10", borderwidth=3, relief="raised")#izquierda arriba derecha abajo
frame9.grid(column=0, row=3)

frame10 = ttk.Frame(frame1, padding="112 10 213 35", borderwidth=3, relief="raised")#izquierda arriba derecha abajo
frame10.grid(column=0, row=4)

firsLabel = ttk.Label(frame7, text="FIRST NAME: ")
firsLabel.grid(column=0, row=0)

firstEntry = ttk.Entry(frame7, width=12)
firstEntry.grid(column=1, row=0)

lastLabel = ttk.Label(frame7, text="LAST NAME: " )
lastLabel.grid(column=2, row=0, padx=3)

lasEntry = ttk.Entry(frame7, width=17)
lasEntry.grid(column=3, row=0)

birtLabel = ttk.Label(frame7, text="BITRH DATE:" )
birtLabel.grid(column=0, row=1, pady=20)

dEntry = ttk.Entry(frame7, width=2)
dEntry.grid(column=1,row=1, sticky=W)

mEntry = ttk.Entry(frame7, width=2)
mEntry.grid(column=1,row=1)

yEntry = ttk.Entry(frame7, width=2)
yEntry.grid(column=1,row=1, sticky=E)

cLabel = ttk.Label(frame7, text="COUNTRY:" )
cLabel.grid(column=2, row=1, pady=20)

cEntry = ttk.Entry(frame7, width=12)
cEntry.grid(column=3,row=1, sticky=W)

creLabel = ttk.Label(frame8, text="CREDIT CARD(IF ANY):")
creLabel.grid(column=0, row=0)

crediEntry = ttk.Entry(frame8, width=20)
crediEntry.grid(column=1, row=0)

cardLabel = ttk.Label(frame8, text=" CREDIT CARD TYPE(IF ANY):")
cardLabel.grid(column=0, row=1, pady=20)

v = Radiobutton(frame8, text="VISA")
v.grid(column=1, row=1)

mas = Radiobutton(frame8, text=" MASTERCARD")
mas.grid(column=2, row=1)

roomLabel = ttk.Label(frame9, text="ROOM TYPE:")
roomLabel.grid(column=0, row=0)

nor = Radiobutton(frame9, text="NORMAL")
nor.grid(column=1, row=0)

fam = Radiobutton(frame9, text="FAMILIAR")
fam.grid(column=1, row=1)

sp = Radiobutton(frame9, text=" SPECIAL")
sp.grid(column=1, row=2)

tLabel = ttk.Label(frame9, text="TOTAL STAYING TIME(DAYS):")
tLabel.grid(column=2, row=0, padx=20)

toEntry = ttk.Entry(frame9, width=5)
toEntry.grid(column=3, row=0)

button = ttk.Button(frame10, text="SUBMIT",).grid(column=1, row=0)

frame0 = ttk.Label(frame6, text="")
frame0.grid(column=0, row=0, padx=50)

frame4= ttk.Label(frame10, text="")
frame4.grid(column=0, row=0, padx=50)    
  

raiz.mainloop()
