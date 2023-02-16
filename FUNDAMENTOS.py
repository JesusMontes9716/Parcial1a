def nuevoTema(tema):
    print("\n=========", tema, "=========\n")


nuevoTema("Operadores Aritmeticos")
print("operador division entera (10//3): " , 10//3) #oparador //
print("operador potencia (5 ** 3): " , 5 ** 3) #operador **


print('-----------------------------------------------------------------------------------------------------')
nuevoTema("Operadores Logicos")
print("operador and (true and false): ", True and False) #operador and


print('-----------------------------------------------------------------------------------------------------')
nuevoTema("Operadores de comparacion ")
print("2 > 3", 2 > 3) # operador >
print("2 >= 3", 2 >= 3) # operador >=
print("2 < 3", 2 < 3) # operador <
print("2 <= 3", 2 <= 3) # operador <=
print("2 == 3", 2 == 3) # operador ==
print("2 != 3", 2 != 3) # operador !=

print('-----------------------------------------------------------------------------------------------------')

nuevoTema("Variables")
variable1=10
_variable2=6.2456
Variable3="juancho"
dosPalabras="Hola"
dos_palabras="Hello"


print(variable1, _variable2, Variable3, dosPalabras, dos_palabras)
a, b, c = 10, 5.16, "Plabra"
print(a, b, c)

print('-----------------------------------------------------------------------------------------------------')

nuevoTema("Enteros")
w = 105
x = 9898259827985732
y = -265
z = 0b00110011
h = 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

print('-----------------------------------------------------------------------------------------------------')

nuevoTema("Flotantes")
x = 1297.50
print(x, type(x))
y = 0.5637939
print(y, type(y))

print('-----------------------------------------------------------------------------------------------------')

nuevoTema(" Nuemeros Complejos")
x = -46j 
y = 12 + 45j
z= 2j 
print(x, type(x))
print(y, type(y))
print(z, type(z))
0
print('-----------------------------------------------------------------------------------------------------')

nuevoTema(" Booleanos")

lis = [8]
print(lis, "es", bool(lis))

t = ()
print(t,"es",bool(t))

new = "Hello"
print(new,"es",bool(new))

num = 99
print(num,"es",bool(num))

comp = 1 + 0j
print(comp,"es",bool(comp))

val = None
print(val,"es",bool(val))

print('-----------------------------------------------------------------------------------------------------')


nuevoTema(" Listas ") # NO son arreglos

a = [10, 20.5, "Python list"]
print(a)
print(a[1])

a[0] = "Hola"
print(a)

print('-----------------------------------------------------------------------------------------------------')

nuevoTema("Tuplas")

t = (25, "tupla",1 + 10j, 3.1416 )
print(t)
print(t[2])
print("t[0:2]:", t[0:2])
# t[1] = 34 operacion no valida en tuplas, no se puede utilizar 
print('-----------------------------------------------------------------------------------------------------')

nuevoTema("Conjuntos")
t = {50, 20, 30, 40, 10, 50}
print("t = ", t)
print(type(t))

print('-----------------------------------------------------------------------------------------------------')

nuevoTema("Diccionarios")
d = {1:"valor1","valor2":2j}
print(d,type(d))
##print("d[valor2]:",d"[valor2]")

print('-----------------------------------------------------------------------------------------------------')

nuevoTema("Cadenas")
cadena1 = "cadena con doble comilla"
cadena2 = 'cadena con comillas simples'
cadena3 = '''esta es una cadena 
de varias lineas con tabulares y
saltos'''
print(cadena1, type(cadena1))
print(cadena2, type(cadena2))
print(cadena3, type(cadena3))
print("segmentacion de cadenas")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:]) 
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1 = "hola"
cadena4 = (cadena1 + " ")*5
print(cadena4)
cadena5 = cadena4.capitalize()
print(cadena5)


print('-----------------------------------------------------------------------------------------------------')

# Activida 1: imprimir la tabla de verda de operadores logicos and, or, not 

print("===== Actividad 1 ======")

booleanos = [False, True]

# Tabla de verdad de or

print('x\ty\tx or y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x or y, sep = '\t')

print()

# Tabla de verdad de and

print('x\ty\tx and y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x and y, sep = '\t')
        
print()

# Tabla de verdad de not

print('x\tnot x')
print('-'*13)
for x in booleanos:
    print(x, not x, sep = '\t')

print()

# Tabla de verdad de ^

print('x\ty\tx ^ y')
print('-'*21)
for x in booleanos:
    for y in booleanos:
        print(x, y, x ^ y, sep = '\t') 






        