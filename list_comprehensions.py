numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares
for numero in numeros:
    # Revisamos si es un número par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista pares: {lista_pares}')

# Mismo ejercicio pero con list comprehensions
# [expresion for var in colección if condición]
# La condición es if es opcional.

lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'Lista pares list_comprehensions: {lista_pares}')


# Ejemplo similar pero con 2 condiciones
# Solo se agregará el valor a la lista cuando este cumple las 2 condiciones
# debe ser divisible entre 2 y también entre 6
pares = [numero for numero in range(50) if (numero % 2 == 0) if (numero % 6 == 0) ]
print(f'Lista div2 div6 list_comprehensions: {pares}')

# Agregando if else, metodo básico
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Lista pares: {lista_pares}')
print(f'Lista impares: {lista_impares}')

# Agregando if else, metodo list comprehensions
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero) for numero in range(10)]
print(f'Lista pares LC: {lista_pares}')
print(f'Lista impares LC: {lista_impares}')


# Lista de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9,10]]
# Convertir la lista de listas en una sola lista
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f'Lista simple: {lista_simple}')

# Ahora creamos una lista de numeros pares a partir de la lista_listas
# Sin list comprehensions, ciclos for anidados
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor % 2 == 0:
            lista_pares.append(valor)
print(f'Lista pares: {lista_pares}')
# Con list comprehensions, en una sola línea de código (opcional)
lista_pares=[]
lista_pares = [valor
               for sublista in lista_listas
               for valor in sublista
               if valor % 2 == 0]
print(f'Lista pares: {lista_pares}')
