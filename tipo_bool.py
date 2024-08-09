# Bool contiene los valores de True y False
# Tipos numéricos, False para 0, True para los demás valores
valor = 1
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')

# Tipo str, False para '', True para cualquier otro valor
valor = ''
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')

# Tipo colecciones, False para vacías,
# True para cualquier otro valor
valor = [] #Lista
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')
valor = (1,) #Tupla
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')
valor = {'Jan':1, 'manuela':2} #Diccionario
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')

if 'hola':
    print(f'Regresó verdadero')
else:
    print(f'Regresó falso')

while resultado:
    print(f'Ejecución ciclo while')
    break
else:
    print(f'Fin ciclo while')