from tkinter import*
from tkinter import ttk
import tkinter as tk


raiz = Tk()
raiz.config(bg="gray39")

imagen1 = PhotoImage(file="c.png")

frame1 = Frame(raiz, bg="gray39", width=650, height=180)
frame1.grid(column=0, row=0)

mainFrame = Frame(raiz, bg="brown4",width=590, height=200)
mainFrame.grid(column=0, row=2, pady=8)

frame2 = Frame(mainFrame, bg="black", width=650, height=90)
frame2.grid(column=0, row=1, padx=40)

frame3 = Frame(frame2, bg="brown4",width=350, height=190)
frame3.grid(column=0, row=0)

frame4 = Frame(frame2, bg="brown4",width=300, height=190)
frame4.grid(column=1, row=0)



frame6 = Frame(mainFrame, bg="brown4",width=590, height=200)
frame6.grid(column=0, row=2, pady=20)




e1 =Label(frame1, bg="gray39")
e1.grid(column=0, row=0)
e1['image']= imagen1


eT = Label(frame1, bg="gray39", fg="white", text="PRODUCT MANAGEMENT", font=( 35))
eT.grid(column=1, row=0, padx=12)

i = Label(frame3, text="ID PRODUCT :", fg="white",bg="brown4", font=( 15), height=2)
i.grid(column=0, row=0, padx=5, sticky=W)

n = Label(frame3, text="NAME :", fg="white",bg="brown4", font=( 15))
n.grid(column=0, row=1, padx=5, sticky=W)

d = Label(frame3, text="DESCRIPTION :", fg="white",bg="brown4", font=( 15))
d.grid(column=0, row=2, padx=5, sticky=W)

q = Label(frame3, text="QUANTITY :", fg="white",bg="brown4", font=( 15))
q.grid(column=0, row=3, padx=5, sticky=W)

p = Label(frame3, text="PRICE :", fg="white",bg="brown4", font=( 15))
p.grid(column=0, row=4, padx=5, pady=1, sticky=W)

iEntry = Entry(frame3, bg="brown4", width=30, fg="white")
iEntry.grid(column=1, row=0, padx=20)

nEntry = Entry(frame3, bg="brown4", width=30, fg="white")
nEntry.grid(column=1, row=1, padx=20)

dEntry = Entry(frame3, bg="brown4", width=30, fg="white")
dEntry.grid(column=1, row=2, padx=20)

qEntry = Entry(frame3, bg="brown4", width=30, fg="white")
qEntry.grid(column=1, row=3, padx=20)

pEntry = Entry(frame3, bg="brown4", width=30, fg="white")
pEntry.grid(column=1, row=4, padx=20)


s = Button(frame4, text="SAVE", fg="white",bg="green", font=( 15), width=15)
s.grid(column=0, row=1, pady=6)

d = Button(frame4, text="DELETE", fg="white",bg="red", font=( 15), width=15)
d.grid(column=0, row=2, pady=5)

u = Button(frame4, text="UPDATE", fg="white",bg="Orange", font=( 15), width=15)
u.grid(column=0, row=3)


tabla = ttk.Treeview(frame6, height=8, columns=("1", "2", "3", "4"))
tabla.column("#0", width=105)
tabla.column("1", width=110, anchor=CENTER)
tabla.column("2", width=110, anchor=CENTER)
tabla.column("3", width=110, anchor=CENTER)
tabla.column("4", width=105, anchor=CENTER)

tabla.heading("#0", text="ID_PRODUCT", anchor=CENTER)
tabla.heading("1", text="NAME_P", anchor=CENTER)
tabla.heading("2", text="DESCRIPTION", anchor=CENTER)
tabla.heading("3", text="QUANTITY", anchor=CENTER)
tabla.heading("4", text="UNITE_PRICE", anchor=CENTER)



tabla.insert("", END, text="1", values=("CONDIA", "LAIT", "24", "$100.0"))
tabla.insert("", END, text="2", values=("LA VACHE QUIRIT", "FROMAGE", "200", "$300.0"))
tabla.insert("", END, text="3", values=("HAMOUD BOUALAM", "BOISSON GASEUSE", "98", "$90.0"))
tabla.insert("", END, text="4", values=("MINA", "CHOCOLAT", "80", "$50.0"))
tabla.insert("", END, text="5", values=("AROMA", "CAFE", "60", "$80.0"))
tabla.insert("", END, text="6", values=("FACTO", "FACTO", "7000", "$600.0"))


tabla.pack() 

barra = Scrollbar(tabla, width=17).place(x=523, y=1)



raiz.mainloop()
        