def factorize_number(n):
    # Lista para almacenar los factores
    factors = []
    # Dividir por 2 hasta que no sea divisible
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Probar con números impares desde 3 en adelante
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    # Si queda un número mayor a 2, es un factor primo
    if n > 2:
        factors.append(n)
    return factors

# Ejemplo de uso
# print(factorize_number(56))  # Salida: [2, 2, 2, 7]

# Ejemplo de uso de listas
def list_example():
    # Crear una lista
    my_list = [1, 2, 3, 4, 5]
    print("Lista original:", my_list)
    
    # Agregar un elemento
    my_list.append(6)
    print("Después de agregar 6:", my_list)
    
    # Eliminar un elemento
    my_list.remove(3)
    print("Después de eliminar 3:", my_list)
    
    # Acceder a un elemento por índice
    print("Elemento en el índice 2:", my_list[2])
    
    # Iterar sobre la lista
    print("Elementos de la lista:")
    for item in my_list:
        print(item)

# Llamar al ejemplo
# list_example()

# Ejemplo de uso de list(range(5))
def range_example():
    # Crear una lista con números del 0 al 4
    my_range_list = list(range(5))
    print("Lista generada con range(5):", my_range_list)

# Llamar al ejemplo
# range_example()

# Ejemplo de uso de un bucle for
def for_loop_example():
    # Iterar sobre una lista
    my_list = [10, 20, 30, 40, 50]
    print("Iterando sobre una lista:")
    for item in my_list:
        print(item)
    
    # Iterar sobre un rango de números
    print("Iterando sobre un rango de números:")
    for i in range(5):
        print(i)

# Llamar al ejemplo
# for_loop_example()

a, b, c = map(int, input("Introduzca los números: ").split())
print("Los números son: ", end = " ")
print(a, b, c)
