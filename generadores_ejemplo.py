# Generador de números del 1 al 5
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda ejecución')

# Utilizar el generador
generador = generador_numeros()
print(f'Objeto generador: {generador}')
print(type(generador))

# Consumir todos los valores del generador
for val in generador_numeros():
    print(f'Numero generado: {val}')

# Otra forma de consumir un generador
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Impresión valor generado while: {valor}')
    except StopIteration as e:
        print('Se terminó de iterar el generador')
        break