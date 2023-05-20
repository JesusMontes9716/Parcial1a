import sqlite3

conexion = sqlite3.connect ('Ejemplo.db')
c = conexion.cursor()


for row in c.execute("SELECT * FROM acciones WHERE operacion = 'compra' "):
    print(row)

conexion.close()
