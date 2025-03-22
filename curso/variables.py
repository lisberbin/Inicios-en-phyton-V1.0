# Declaración de variables en Python

# Entero
numero_entero = 10

# Flotante
numero_flotante = 3.14

# Cadena
texto = "Hola, mundo"

# Booleano
es_valido = False

# Lista
lista = [1, 2, 3, 4, 5]

# Diccionario
diccionario = {"clave": "lisbeth", "edad": 25}

# Tupla
tupla = (1, 2, 3)

# Conjunto
conjunto = {1, 2, 3, 4, 5}

# Imprimir variables
print("Esto es concatenar con , ",diccionario.get("edad"))
print(tupla[0])
print(lista.__getitem__(0))
if es_valido:
    print("Es válido")
else:  
    print(conjunto.pop()+1)
    
# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"
# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2
# Realizamos unas operaciones con a,b,c
d = (a + b) * c
# Definimos una variable booleana
imprimir = True
# Si imprimir, print()
if imprimir:
 print(x, d)
# Salida: El valor de (a+b)*c es 14

"""_summary_ probando comentarios
"""
# Aceptar declaraciones de variables en una sola línea
a, b, c = 1, 2, 3
print(a, b, c)  # Salida: 1 2 3
# Aceptar asignaciones múltiples
a = b = c = 4
print(a, b, c)  # Salida: 4 4 4
# Aceptar asignaciones múltiples con diferentes valores
a, b = 1, 2
print(a, b)  # Salida: 1 2
# Intercambiar valores de dos variables
a, b = b, a
print(a, b)  # Salida: 2 1
x = 5; y = 10
print(x, y)  # Salida: 5 10

# definiedo funciones
def mifuncion(a, b, c):
 return a+b+c
d = mifuncion(10,23,3)
print(d)  # Salida: 36

def en_pantalla(frase1, frase2):
    print(frase1, frase2) # "return" no es obligatorio
#en_pantalla('Me gusta', 'Python')

def suma(a, b): # Definimos lafunción "suma". Tiene 2 parámetros.
    return a+b # "return" devuelveel resultado de la función.
suma (2, 3) # Función con ints
# Resultado = 5
suma(2.7, 4.0) # Función con floats
# Resultado = 6.7
print(suma('Me gusta', 'Python')) # Función con strings


def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print(x) # Llamamos a f2 desde f1
    f2(b)
f1('Python') 

def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
print(factorial(5))

def hallar(x):
    if x%2 == 0 or x%3 == 0:
        print("divisible")
    
hallar(9)

#trabajando con operadores matematicos

def maxmin(lista):
    return max(lista), min(lista)
#Devuelve una tupla de 2 elementos
l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(l) 
#Desempaqueta la tupla en 2 variables
print(minimo, maximo, sep= ' ')



la = [1, 2, 3, 4, 5]
lb = list('abcde')
lc = list(range(5))
print(la, lb, lc)

a={'a':1, 'b':2, 'c':3}
monedas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(moneda)
#monedas.get('Euro', 'No se encuentra')
print(monedas.get(moneda.title(), 'No se encuentra'))

datos={'Nombre':'', 'Edad':0, 'Direccion':'', 'Telefono':''}
datos['Nombre'] = input('Introduce tu nombre: ')
datos['Edad'] = input('Introduce tu edad: ')
datos['Direccion'] = input('Introduce tu dirección: ')
datos['Telefono'] = input('Introduce tu teléfono: ')
print(datos.get('Nombre'),"tiene ",datos.get('Edad'),"años, vive en ", datos.get('Direccion'), "y su número de teléfono es ",datos.get('Telefono'))

s='Me gusta Python'
for c in s:
    print(c, end=' ')
for s in ['Me', 'gusta', 'Python']:
    print(s, end=' ')

