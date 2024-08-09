# Profundizando en diccionarios

# diccionario(mutable) = llave(inmutable): valor(mutable)
# Los diccionarios guardan un orden, a diferencia de un set.
diccionario = {'Nombre':'Juan', 'Apellido':'Perez','Edad':28}
# print(diccionario)

# Los dict son mutables, pero las llaves deben ser inmutables.
# diccionario = {[1,2]:'Valor1'} # La llave es una lista, un elemento mutable y marca error
# diccionario = {(1,2):'Valor1'} # La llave es una tupla, un elemento inmutable y no marca errores
# print(diccionario)

diccionario['Departamento'] = 'Sistemas' # agregar una llave y su valor.
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario. En los value sí.
# Si se agrega un valor a una llave ya existente, se reemplaza el valor.

diccionario['Nombre'] = 'Juankrlo' # agregar una llave y su valor, pero como ya existe, reemplaza el valor.
print(diccionario)


# Recuperar un valor indicando la llave
print(diccionario['Nombre'])
# Si no encuentra la llave, lanza una exception
# print(diccionario['Nombr'])


# Método get recupera una llave, y si no existe NO lanza exception
# además podemos regresar un valor en caso de que no exista la llave.
print(diccionario.get('Nombre','No se encontró la llave')) # Si no encuentra la llave, envía valor después de la coma.

# setdefault sí modifica el diccionario, además de agregar un valor por default si no la encuentra y la crea.
nombre = diccionario.setdefault('Nombre','Valor por default')
print(nombre)
print(diccionario)

# Imprimir con pprint
from pprint import pprint as pp
pp(diccionario, sort_dicts=0) #Por defecto organiza las llaves.