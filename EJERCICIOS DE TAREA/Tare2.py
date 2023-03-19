from tkinter import*
from tkinter import ttk
import tkinter as tk


raiz = Tk()
raiz.config(bg="gray39")

imagen1 = PhotoImage(file="c.png")
imagen2 = PhotoImage(file="l.png")
imagen3 = PhotoImage(file="lim.png")
imagen4 = PhotoImage(file="b.png")

frame1 = Frame(raiz, bg="gray39", width=650, height=180)
frame1.grid(column=0, row=0)

mainFrame = Frame(raiz, bg="saddle brown",width=590, height=200)
mainFrame.grid(column=0, row=2, pady=8)

frame2 = Frame(mainFrame, bg="black", width=650, height=90)
frame2.grid(column=0, row=1, padx=40)

frame3 = Frame(frame2, bg="saddle brown",width=350, height=190)
frame3.grid(column=0, row=0)

frame4 = Frame(frame2, bg="saddle brown",width=300, height=190)
frame4.grid(column=1, row=0)

frame5 = Frame(frame4, bg="saddle brown")
frame5.grid(column=0, row=0)

frame6 = Frame(mainFrame, bg="saddle brown",width=590, height=200)
frame6.grid(column=0, row=2, pady=20)




e1 =Label(frame1, bg="gray39")
e1.grid(column=0, row=0)
e1['image']= imagen1

b2 =Button(frame5, borderwidth=0)
b2.grid(column=0, row=0,padx=7)
b2['image']= imagen2

b3 =Button(frame5, borderwidth=0)
b3.grid(column=1, row=0,padx=7)
b3['image']= imagen3

b4 =Button(frame5, borderwidth=0)
b4.grid(column=2, row=0, padx=7)
b4['image']= imagen4

eT = Label(frame1, bg="gray39", fg="white", text="PRODUCT MANAGEMENT", font=( 35))
eT.grid(column=1, row=0, padx=12)

i = Label(frame3, text="ID PRODUCT :", fg="white",bg="saddle brown", font=( 15), height=2)
i.grid(column=0, row=0, padx=5, sticky=W)

n = Label(frame3, text="NAME :", fg="white",bg="saddle brown", font=( 15))
n.grid(column=0, row=1, padx=5, sticky=W)

d = Label(frame3, text="DESCRIPTION :", fg="white",bg="saddle brown", font=( 15))
d.grid(column=0, row=2, padx=5, sticky=W)

q = Label(frame3, text="QUANTITY :", fg="white",bg="saddle brown", font=( 15))
q.grid(column=0, row=3, padx=5, sticky=W)

p = Label(frame3, text="PRICE :", fg="white",bg="saddle brown", font=( 15))
p.grid(column=0, row=4, padx=5, pady=1, sticky=W)

iEntry = Entry(frame3, bg="saddle brown", width=30, fg="white")
iEntry.grid(column=1, row=0, padx=20)

nEntry = Entry(frame3, bg="saddle brown", width=30, fg="white")
nEntry.grid(column=1, row=1, padx=20)

dEntry = Entry(frame3, bg="saddle brown", width=30, fg="white")
dEntry.grid(column=1, row=2, padx=20)

qEntry = Entry(frame3, bg="saddle brown", width=30, fg="white")
qEntry.grid(column=1, row=3, padx=20)

pEntry = Entry(frame3, bg="saddle brown", width=30, fg="white")
pEntry.grid(column=1, row=4, padx=20)


s = Button(frame4, text="SAVE", fg="white",bg="green", font=( 15), width=15)
s.grid(column=0, row=1, pady=6)

d = Button(frame4, text="DELETE", fg="white",bg="red", font=( 15), width=15)
d.grid(column=0, row=2, pady=5)

u = Button(frame4, text="UPDATE", fg="white",bg="DarkOrange1", font=( 15), width=15)
u.grid(column=0, row=3)


tabla = ttk.Treeview(frame6, height=8, columns=("col1", "col2", "col3", "col4"))
tabla.column("#0", width=105)
tabla.column("col1", width=110, anchor=CENTER)
tabla.column("col2", width=110, anchor=CENTER)
tabla.column("col3", width=110, anchor=CENTER)
tabla.column("col4", width=105, anchor=CENTER)

tabla.heading("#0", text="ID_PRODUCT", anchor=CENTER)
tabla.heading("col1", text="NAME_P", anchor=CENTER)
tabla.heading("col2", text="DESCRIPTION", anchor=CENTER)
tabla.heading("col3", text="QUANTITY", anchor=CENTER)
tabla.heading("col4", text="UNITE_PRICE", anchor=CENTER)



tabla.insert("", END, text="1", values=("Condia", "lait", "24", "100.0"))
tabla.insert("", END, text="2", values=("la vache quirit", "fromage", "200", "300.0"))
tabla.insert("", END, text="3", values=("hamoud boualam", "boisson gaseuse", "98", "90.0"))
tabla.insert("", END, text="4", values=("Mina", "chocolat", "80", "50.0"))
tabla.insert("", END, text="5", values=("Aroma", "cafe", "60", "80.0"))
tabla.insert("", END, text="6", values=("Facto", "facto", "7000", "600.0"))


tabla.pack()

barra = Scrollbar(tabla, width=17).place(x=523, y=1)



raiz.mainloop()
        