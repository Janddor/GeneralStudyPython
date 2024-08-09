# Expresion generadora (es un generador anónimo)
# valor*valor es lo mismo que yield valor*valor
multiplicacion = (valor*valor for valor in range(4))
print(type(multiplicacion)) # Es un generador

print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

# También se puede pasar una expresión generadora a una función
# (sin parénteais)
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')

# También podemos usar una lista o cualquier otro iterador
lista = ['Juan', 'Perez']
generador = (valor for valor in lista)
print(f'Nombre generado: {next(generador)}')
print(f'Nombre generado: {next(generador)}')

# Crear un string a partir de un generador, creado a partir de una lista
lista = ['Karla', 'Gomez']
contador = 0
def incrementar():
    global contador
    contador += 1
    return contador
# La primera parde es el yield, la segunda parte es el for, entre paréntesis
generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada a partir de la lista: {lista}')