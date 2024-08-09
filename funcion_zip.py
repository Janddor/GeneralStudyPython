# Función ZIP
# print(*dir(__builtins__), sep='\n')  # métodos o funciones built-in en python

# numeros = [1,2,3]
# letras = ['a', 'b', 'c','d']
# identificadores = 321, 322, 323, 324, 325
# conjunto = {6, 0, 4, 9, 8, 15, 10}
# mezcla = list(zip(numeros, letras, identificadores, conjunto))
# print(f'Mezcla: {mezcla}, tipo: {type(mezcla)}')
#
# # iterar en paralelo
# for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
#     print(f'Numero: {numero}, '
#           f'Letra: {letra}, '
#           f'Id: {id}, '
#           f'Aleatorio: {aleatorio}')
#
# nueva_lista = []
# for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
#     nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
# print(nueva_lista)
#
# # unzip
# mezcla = [(1,'a'),(2,'b'),(3,'c')]
# numeros, letras = zip(*mezcla)
# print(f'Numeros: {numeros} Letras: {letras}')
#
# # ordenamiento usando zip
# letras = ['c', 'd', 'a', 'e', 'b']
# numeros = [3,2,4,1,0]
# mezcla = zip(letras, numeros)
# print(tuple(mezcla)) # sin ordenar
# print(sorted(zip(letras, numeros))) #ordenando con el primer elemento del zip


# Crear un diccionario con zip y dos iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores =['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

# Actualizar un elemento de un diccionario
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave,nueva_edad))
print(diccionario)





