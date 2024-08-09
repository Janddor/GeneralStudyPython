# Generadores
# Es una función especial, retorna una secuencia de valores
# suspende la ejecución de la función yield (producir)
# (no se usa return)
def generador():
    yield 1
    print(f'Reanudando')
    yield 2
    print(f'Reanudando')
    yield 3

# Consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen),'\n')
# Si tratamos de consumir más valores de los que produce
# marcará un error de StopIteration
# Se tendría que volver a llamar el generador: gen = generador()

# Consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'Número generado: {valor}')

