import sqlite3

conexion = sqlite3.connect ('Datos.db')
c = conexion.cursor()

c.execute ("SELECT * FROM Datos")
print (c.fetchone())
print (c.fetchone())
print (c.fetchone())
print (c.fetchone())
print (c.fetchone())
conexion.close()