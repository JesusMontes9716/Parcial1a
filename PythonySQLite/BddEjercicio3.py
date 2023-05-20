import sqlite3

conexion = sqlite3.connect ('Ejemplo.db')

c = conexion.cursor()

c.execute ("INSERT INTO acciones VALUES ('12/sep/2023', 'compra', 'INV', 200, 30)")
c.execute ("INSERT INTO acciones VALUES ('4/mar/2023', 'compra', 'INV', 300, 45)")
c.execute ("INSERT INTO acciones VALUES ('5/feb/2023', 'compra', 'INV', 250, 38)")
c.execute ("INSERT INTO acciones VALUES ('6/jun/2023', 'compra', 'INV', 50, 7.5)")
c.execute ("INSERT INTO acciones VALUES ('7/dic/2023', 'compra', 'INV', 120, 18)")


conexion.commit ()

conexion.close()
