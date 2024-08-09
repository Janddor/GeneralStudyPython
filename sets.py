# Profundizar en set
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables

# conjunto = {(1,2), (3,4)} # Tuplas son inmutables, listas son mutables y marcaría error
# conjunto = {'Juan', True, 18.0} # Puros elementos inmutables
#
# # Set vacío
# conjunto = {} #Esto crea un diccionario, no un set.
# print(type(conjunto))
# conjunto = set()
# print(type(conjunto))
#
# # Un set es mutable
# conjunto.add('Juan')
# print(conjunto)
# conjunto.add('Juan') #Como ya existe  no se repite, toma solo un 'Juan'
# print(conjunto)
#
# # Crear un set a partir de un iterable
# conjunto = set([4,5,6,7,4])
# print(conjunto)
# # Podemos agregar más elementos o incluso otro set
# conjunto2 = {100, 200, 300, 300}
# conjunto.update(conjunto2)
# print(conjunto)
# conjunto.update([20, 30, 40, 40, 40])
# print(conjunto)

# Copiar un set (copiar poco profunda, solo copia referencias) pero diferente id.
# conjunto_copia = conjunto.copy()
# print(id(conjunto_copia))
# print(id(conjunto))

# Operaciones de conjuntos con set
# Personas con distintas características
pelo_negro = {'Juan', 'Karla', 'Pedro', 'María'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'María'}

# (Union) Todos con ojos_cafe y pelo rubio (No se repiten elementos)
print(ojos_cafe.union(pelo_rubio))
print(pelo_rubio.union(ojos_cafe))# (conmutativa), no importa el orden de la union

# (intersection) solo personas con ojos café y pelo rubio (conmutativa)
print(ojos_cafe.intersection((pelo_rubio)))

# (Difference) (No es conmutativa, el orden si importa)
# Personas que se encuentran en el primer set pero no en el segundo
# Es decir tomar de pelo_negro todos los que no tengan ojos_cafe
print(pelo_negro.difference(ojos_cafe))

# (Symmetric Difference) Personas con pelo negro o ojos café, pero no ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

# (subset) Preguntar si un set está contenido en otro
print(f'Todos los menores de 30 son de pelo negro: {menores_30.issubset(pelo_negro)}')

# (superset) Preguntar si un set contiene a otro set (inverso de subset)
print(f'Las personas de pelo negro son menores de 30: {menores_30.issuperset(pelo_negro)}')

# (disjoint) Preguntar si un set tiene elementos en comun con otro set
print(f'Las personas de pelo negro no tienen pelo rubio: {pelo_negro.isdisjoint(pelo_rubio)}')


