# Profundizando en el tipo float
a = 3.0
# print(f'a: {a:.2f}') # :.2f significa darle formato de 2 puntos flotante.
# Constructor float puede recibir int y str
a = float('10')#El constructor está sobrecargado por lo que permite varios tipos de dato de entrada.
print(f'a: {a:.2f}')
a = float(10)
print(f'a: {a:.2f}')
# Notación exponencial (valores positivos o negativos)
a = 3e5
print(f'a: {a:.2f}')
a = 3e-5
print(f'a: {a:.6f}')
# SI en un cálculo hay un float, toda la expresión se vuelve float.
a = 4.0 + 5
print(f'resultado a: {a}')