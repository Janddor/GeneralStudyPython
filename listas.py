# Profundizando listas
# Listas son mutables

# nombres1 = ['Juan', 'Karla', 'Pedro']
# nombres2 = 'Laura María Gonzalo Ernesto'.split()
# # Sumar listas
# print(f'Sumar listas{nombres1+nombres2}')
# # Extender una lista con otra lista
# nombres1.extend(nombres2)
# print(f'Extender la lista1 con lista2{nombres1}')
#
# # Lista de números
# numeros1 = [10, 40, 15, 4, 20, 90, 4]
# print(f'Lista original: {numeros1}')
# # Función index - obtiene el índice del primer elemento encontrado en la lista
# # help(list.index)
# print(f'Indice 4: {numeros1.index(4)}')
#
# # Invertir el orden de los elementos de una lista
# numeros1.reverse()
# print(f'Lista invertida: {numeros1}')
# print(f'Indice 4: {numeros1.index(4)}')
#
# # Ordernar elementos asc o desc
# numeros1.sort()
# print(f'Lista ordenada ascendente: {numeros1}')
# numeros1.sort(reverse=1)
# print(f'Lista ordenada descendente: {numeros1}')
#
# # Obtener min y max de una lista
# print(f'Valor mínimo: {min(numeros1)}')
# print(f'Valor máximo: {max(numeros1)}')
#
# # Copiar los elementos de una lista
# numeros2 = numeros1.copy()
# # help(list.copy)
# print(f'Misma referencia?: {numeros1 is numeros2}')
# print(f'Mismo contenido?: {numeros1 == numeros2}')
#
# # Usando el constructor de la lista
# numeros2 = list(numeros1) # Nuevo espacio de memoria
# print(f'Misma referencia?: {numeros1 is numeros2}')
# print(f'Mismo contenido?: {numeros1 == numeros2}')
#
# # slicing
# numeros2 = numeros1[:]
# print(f'Misma referencia?: {numeros1 is numeros2}')
# print(f'Mismo contenido?: {numeros1 == numeros2}')

# # Multiplicación listas
# lista_multiplicacion = 5*[[2,5]]
# print(f'Lista: {lista_multiplicacion}')
# print(f'Misma referencia? {lista_multiplicacion[0] is lista_multiplicacion[1]}')
# print(f'Mismo contenido ? {lista_multiplicacion[0] == lista_multiplicacion[1]}')
# # Todos los elementos multiplicados apuntan a la misma ref
# lista_multiplicacion[2].append(1) #Le escribe a la dirección en la que esté lista[2]
# #la cual es la misma dirección para todos.
# print(f'Lista: {lista_multiplicacion}')


# # Matrices
# matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
# print(f'Matriz original: {matriz}')
# print(f'Renglon 0, col 0: {matriz[0][0]}')
# print(f'Renglon 2, col 2: {matriz[2][2]}')
# matriz[2][0] = 61
# print(f'Matriz Modificada: {matriz}')

lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')

# Ordenamiento utilizando sorted built-in
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1) #Ascendente
print(f'{nombres1}')
nombres1 = sorted(nombres1, reverse=1) #Descendente
print(f'{nombres1}')
nombres1 = sorted(nombres1, key=len) #Asc segun largo de cadenas
print(f'{nombres1}')
# built-in reversed
nombres1 = list(reversed(nombres1))
print(f'{nombres1}')


