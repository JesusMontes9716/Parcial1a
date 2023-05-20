
from tkinter import *
from tkinter import ttk
import os
import sqlite3

#Objeto persona
class Persona:
    def __init__(self, nombre: str, a_paterno: str, a_materno: str, correo: str, movil: str, ocupacion: str, aficionLeer: bool, aficionMusica: bool, aficionVideojuegos: bool, estado: str):
        self.nombre= nombre
        self.a_paterno= a_paterno
        self.a_materno= a_materno
        self.correo= correo
        self.movil= movil
        self.ocupacion= ocupacion
        self.aficionLeer= aficionLeer
        self.aficionMusica= aficionMusica
        self.aficionVideojuegos= aficionVideojuegos
        self.estado = estado


    def _iter_(self):
        yield self.nombre
        yield self.a_paterno



if not os.path.isfile("Datos.csv"):
    with open("Datos.csv", 'w') as file:
        file.write("Nombre, ApellidoPaterno, Apellidomaterno, Correo, Movil, Ocupacion, Aficiones, Leer, Musica, Videojuegos, Estado\n")
else:
    pass



def mostrar_personas(lista_personas):
    for persona in lista_personas:
        print("Nombre: ", persona.nombre)
        print("Apellido paterno: ", persona.a_paterno)
        print("Apellido materno: ", persona.a_materno)
        print("Correo: ", persona.correo)
        print("Movil: ", persona.movil)
        print("Ocupacion: ", persona.ocupacion)
        print("Aficiones: ")
        print(" Leer: ", persona.aficionLeer)
        print(" Musica: ", persona.aficionMusica)
        print(" Videojuegos: ", persona.aficionVideojuegos)
        print("Estado: ", persona.estado)   
    


    # Limpiar los campos de entrada después de guardar los datos
    nombre.delete(0, END)
    aPaterno.delete(0, END)
    aMaterno.delete(0, END)
    correo.delete(0, END)
    movil.delete(0, END)
    ocupacion.set(None)
    aficionLeer.set(False)
    aficionMusica.set(False)
    aficionVideojuegos.set(False)


# Crear ventana principal
root = Tk()

# Crear una lista vacía para almacenar las personas
personas = []

# Crear un notebook (panel tabulado)
notebook = ttk.Notebook(root)
notebook.configure(width=400, height=500)

# Crear pestañas dentro del notebook
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)


file= open("Datos.csv", "r")
    
#Titulo    
line = file.readline()
#Segunda linea
line = file.readline()
personas = []

while line:

    
    # Dividir la línea en diferentes partes utilizando una coma como separador
    itemProducto = line.strip().split(",")

    # Crear un objeto de la clase Productos con los valores obtenidos de la línea
    persona = Persona(itemProducto[0], itemProducto[1], itemProducto[2], itemProducto[3], itemProducto[4], itemProducto[5], itemProducto[6], itemProducto[7], itemProducto[8], itemProducto[9])

    # Agregar el objeto a la lista de personas
    personas.append(persona)

    # Leer la siguiente línea
    line = file.readline()

    for i, persona in enumerate(personas):
        table = ttk.Treeview(tab3, columns=("nombre", "a_paterno", "a_materno", "correo", "movil", "ocupacion", "aficionLeer", "aficionMusica", "aficionVideojuegos", "estado"))

        # Definir encabezados de columna
        table.heading("#0", text="ID")
        table.heading("nombre", text="Nombre")
        table.heading("a_paterno", text="Apellido paterno")
        table.heading("a_materno", text="Apellido materno")
        table.heading("correo", text="Correo")
        table.heading("movil", text="Móvil")
        table.heading("ocupacion", text="Ocupación")
        table.heading("aficionLeer", text="Lee")
        table.heading("aficionMusica", text="Escucha música")
        table.heading("aficionVideojuegos", text="Juega videojuegos")
        table.heading("estado", text="Estado")

        # Definir anchos de columna
        table.column("#0", width=50)
        table.column("nombre", width=100)
        table.column("a_paterno", width=120)
        table.column("a_materno", width=120)
        table.column("correo", width=200)
        table.column("movil", width=100)
        table.column("ocupacion", width=120)
        table.column("aficionLeer", width=100)
        table.column("aficionMusica", width=120)
        table.column("aficionVideojuegos", width=120)
        table.column("estado", width=120)
            
            
        table.insert(parent="", index=i, iid=i, text=i+1, values=(itemProducto[0], itemProducto[1], itemProducto[2], itemProducto[3], itemProducto[4], itemProducto[5], itemProducto[6], itemProducto[7], itemProducto[8], itemProducto[9]))
file.close()

def guardar():
    # Crear objeto persona con los datos ingresados por el usuario
    persona = Persona(nombre.get(), aPaterno.get(), aMaterno.get(), correo.get(), movil.get(), ocupacion.get(), aficionLeer.get(), aficionMusica.get(), aficionVideojuegos.get(), estado.get())
    # Agregar el objeto a la lista de productos
    personas.append(persona)
    # Guardar datos en un archivo de texto
    with open("Datos.csv", "a") as file:

        if persona.aficionLeer == True:
            leer="Si_lee"
        else:
            leer="No_lee"

        if persona.aficionMusica == True:
            musica="Escucha_Musica"
        else:
            musica="No_Escucha_Musica"

        if persona.aficionVideojuegos == True:
            videojuegos="Juega_Videojuegos"
        else:
            videojuegos="No_ Juega_Videojuegos"
            
        file.write(f"{persona.nombre}, {persona.a_paterno}, {persona.a_materno}, {persona.correo}, {persona.movil}, {persona.ocupacion}, {leer}, {musica}, {videojuegos}, {persona.estado}\n")
        table.insert(parent="", index="end", iid=len(personas), text=len(personas), values=(persona.nombre, persona.a_paterno, persona.a_materno, persona.correo, persona.movil, persona.ocupacion, leer, musica, videojuegos, persona.estado))
    
    '''nombre.delete(0, END)
    aPaterno.delete(0, END)
    aMaterno.delete(0, END)
    correo.delete(0, END)
    movil.delete(0, END)
    ocupacion.set(None)
    aficionLeer.set(False)
    aficionMusica.set(False)
    aficionVideojuegos.set(False)'''   


def BaseDeDatos():
        # Verificar si la base de datos ya existe
    if not os.path.isfile("Datos.db"):
        # Crear la conexión a la base de datos
        conexion = sqlite3.connect("Datos.db")
        cursor = conexion.cursor()

        # Crear la tabla si no existe
        cursor.execute('''CREATE TABLE Datos (
                            id_registro INTEGER PRIMARY KEY,
                            Nombre TEXT,
                            ApellidoPaterno TEXT,
                            ApellidoMaterno TEXT,
                            Correo TEXT,
                            Movil TEXT,
                            Ocupacion TEXT,
                            Leer TEXT,
                            Musica TEXT,
                            Videojuegos TEXT,
                            Estado TEXT
                            )''')
        

        persona = Persona(nombre.get(), aPaterno.get(), aMaterno.get(), correo.get(), movil.get(), ocupacion.get(), aficionLeer.get(), aficionMusica.get(), aficionVideojuegos.get(), estado.get())

        personas.append(persona)

        if persona.aficionLeer == True:
            leer="Si_lee"
        else:
            leer="No_lee"

        if persona.aficionMusica == True:
            musica="Escucha_Musica"
        else:
            musica="No_Escucha_Musica"

        if persona.aficionVideojuegos == True:
            videojuegos="Juega_Videojuegos"
        else:
            videojuegos="No_ Juega_Videojuegos"

        cursor.execute('SELECT COUNT(*) FROM Datos')
        total_registros = cursor.fetchone()[0]

        # Insertar los datos en la base de datos
        cursor.execute("INSERT INTO datos (id_registro, Nombre, ApellidoPaterno, ApellidoMaterno, Correo, Movil, Ocupacion, Leer, Musica, Videojuegos, Estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (total_registros+1,persona.nombre, persona.a_paterno, persona.a_materno, persona.correo, persona.movil, persona.ocupacion, leer, musica, videojuegos, persona.estado))

        print("DATO EN LA BASE DE DATOS: ")

        for row in cursor.execute ("SELECT * FROM Datos"):
            print (row)

        conexion.commit()
        conexion.close()
    else:

        conexion = sqlite3.connect("Datos.db")
        cursor = conexion.cursor()

        persona = Persona(nombre.get(), aPaterno.get(), aMaterno.get(), correo.get(), movil.get(), ocupacion.get(), aficionLeer.get(), aficionMusica.get(), aficionVideojuegos.get(), estado.get())

        # Agregar el objeto a la lista de productos (si es necesario)
        personas.append(persona)

        if persona.aficionLeer == True:
            leer="Si_lee"
        else:
            leer="No_lee"

        if persona.aficionMusica == True:
            musica="Escucha_Musica"
        else:
            musica="No_Escucha_Musica"

        if persona.aficionVideojuegos == True:
            videojuegos="Juega_Videojuegos"
        else:
            videojuegos="No_ Juega_Videojuegos"

        cursor.execute('SELECT COUNT(*) FROM Datos')

        total_registros = cursor.fetchone()[0]
        
        # Insertar los datos en la base de datos
        cursor.execute("INSERT INTO datos (id_registro, Nombre, ApellidoPaterno, ApellidoMaterno, Correo, Movil, Ocupacion, Leer, Musica, Videojuegos, Estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (total_registros+1,persona.nombre, persona.a_paterno, persona.a_materno, persona.correo, persona.movil, persona.ocupacion, leer, musica, videojuegos, persona.estado))
        print("DATOS EN LA BASE DE DATOS: ")
        for row in cursor.execute ("SELECT * FROM Datos"):
            print (row)

        # Guardar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close()
        
def Borrar():
    nombre.delete(0, END)
    aPaterno.delete(0, END)
    aMaterno.delete(0, END)
    correo.delete(0, END)
    movil.delete(0, END)
    ocupacion.set(None)
    aficionLeer.set(False)
    aficionMusica.set(False)
    aficionVideojuegos.set(False)



# Modificar el estilo por defecto de las etiquetas
style = ttk.Style()
style.configure('TLabel', font=('Arial', 14))

# Agregar widgets a cada pestaña
ttk.Label(tab2, text="En reparacion").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab4, text="Sin servicio").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab5, text="Llamale a Dios").grid(column=0, row=0, padx=10, pady=10)

# Agregar las pestañas al notebook
notebook.add(tab1, text="     Add    ")
notebook.add(tab3, text="     Tabla    ")

# Crear un estilo personalizado para las pestañas
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {"background": "skyblue1", "foreground": "black", "font": ("Arial", 14)},
        "map": {"background": [("selected", "Dodgerblue2")], "foreground": [("selected", "white")]}
    }
})
style.theme_use("MyStyle")

# Mostrar el notebook
notebook.pack(expand=True, fill=BOTH)

#Frame 1 (0,0)

BaseFrame = ttk.Frame(tab1, padding="5 30 5 5")
BaseFrame.grid(column=0, row= 0)

# Crear frame principal
main_frame = ttk.Frame(BaseFrame, width=200, height=200)
main_frame.pack()

# Crear frame secundario
sub_frame = ttk.Frame(main_frame, width=300, height=300,padding="30 30 30 30",relief="raised")
sub_frame.pack()
sub_frame.grid(column=0,row=0,pady=25)

ttk.Label(sub_frame, text="Nombre:").grid(column = 0, row=0, pady= 12)
nombre = ttk.Entry(sub_frame, width=20)
nombre.grid(column=1,row=0)

ttk.Label(sub_frame, text="A. Paterno:").grid(column = 0, row=1, pady= 12)
aPaterno = ttk.Entry(sub_frame, width=20)
aPaterno.grid(column=1,row=1)

ttk.Label(sub_frame, text="A. Materno:").grid(column = 0, row=2, pady= 12)
aMaterno = ttk.Entry(sub_frame, width=20)
aMaterno.grid(column=1,row=2)

ttk.Label(sub_frame, text="Correo").grid(column = 0, row=3, pady= 12)
correo = ttk.Entry(sub_frame, width=20)
correo.grid(column=1,row=3)

ttk.Label(sub_frame, text="Movil").grid(column = 0, row=4, pady= 12)
movil = ttk.Entry(sub_frame, width=20)
movil.grid(column=1,row=4)

#

sub_frame2 = ttk.Frame(main_frame, width=300, height=300,padding="10 30 10 30")
sub_frame2.grid(column=1,row=0)

ocupacion= StringVar()

Estudiante_rb= ttk.Radiobutton(sub_frame2,text="Estudiante", variable=ocupacion, value="Estudiante").grid(column = 0, row=0, sticky=(W))
Empleado_rb= ttk.Radiobutton(sub_frame2,text="Empleado", variable=ocupacion, value="Empleado").grid(column = 0, row=1, sticky=(W))
Desempleado_rb= ttk.Radiobutton(sub_frame2,text="Desempleado", variable=ocupacion, value="Desempleado").grid(column = 0, row=2, sticky=(E))



sub_frame3 = ttk.Frame(main_frame, width=300, height=300,padding="30 10 30 10",relief="raised")
sub_frame3.grid(column=0,row=1)


ttk.Label(sub_frame3, text="Aficiones:").grid(column = 0, row=0, pady= 12)


aficionLeer= BooleanVar()
Leer_cb= ttk.Checkbutton(sub_frame3,text="Leer", variable=aficionLeer).grid(column = 0, row=1)

aficionMusica= BooleanVar()
Musica_cb= ttk.Checkbutton(sub_frame3,text="Musica", variable=aficionMusica).grid(column = 1, row=1)

aficionVideojuegos= BooleanVar()
Videojuegos_cb= ttk.Checkbutton(sub_frame3,text="Videojuegos", variable=aficionVideojuegos).grid(column = 2, row=1)


#

sub_frame4 = ttk.Frame(main_frame, width=200, height=300,padding="10 10 10 10")
sub_frame4.grid(column=1,row=1)

estado = StringVar()
comboEstados = ttk. Combobox(sub_frame4, textvariable=estado)
comboEstados.grid(column = 0, row=0)
comboEstados[ 'values'] = ('Aguascalientes','Baja California','Baja California Sur','Campeche',
'Chiapas','Chihuahua','Ciudad de México','Coahuila','Colima','Durango','Guanajuato','Guerrero',
'Hidalgo','Jalisco','México','Michoacán','Morelos','Nayarit','Nuevo León','Oaxaca','Puebla',
'Querétaro','Quintana Roo','San Luis Potosí','Sinaloa','Sonora','Tabasco','Tamaulipas',
'Tlaxcala','Veracruz','Yucatán','Zacatecas')

sub_frame5 = ttk.Frame(main_frame, width=200, height=300,padding="10 10 10 10")
sub_frame5.grid(column=0,row=2)

guardar_button = ttk.Button(sub_frame5, text="Guardar", command=guardar).grid(column = 0, row=0, padx= 12)
ttk.Button(sub_frame5, text="Agregar a Base de Datos", command=BaseDeDatos).grid(column = 1, row=0,padx= 12)
ttk.Button(sub_frame5, text="Borrar", command= Borrar).grid(column = 2, row=0,padx= 12)

# Crear tabla para mostrar lista de personas
table = ttk.Treeview(tab3, columns=("nombre", "a_paterno", "a_materno", "correo", "movil", "ocupacion", "aficionLeer", "aficionMusica", "aficionVideojuegos", "estado"))

# Definir encabezados de columna
table.heading("#0", text="ID")
table.heading("nombre", text="Nombre")
table.heading("a_paterno", text="Apellido paterno")
table.heading("a_materno", text="Apellido materno")
table.heading("correo", text="Correo")
table.heading("movil", text="Móvil")
table.heading("ocupacion", text="Ocupación")
table.heading("aficionLeer", text="Lee")
table.heading("aficionMusica", text="Escucha música")
table.heading("aficionVideojuegos", text="Juega videojuegos")
table.heading("estado", text="Estado")

# Definir anchos de columna
table.column("#0", width=50)
table.column("nombre", width=100)
table.column("a_paterno", width=120)
table.column("a_materno", width=120)
table.column("correo", width=200)
table.column("movil", width=100)
table.column("ocupacion", width=120)
table.column("aficionLeer", width=100)
table.column("aficionMusica", width=120)
table.column("aficionVideojuegos", width=120)
table.column("estado", width=120)
 


# Ubicar tabla en la pestaña
table.pack(fill=BOTH, expand=1)



# Mostrar ventana
root.mainloop()
