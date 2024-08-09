# Funciones anidadas
# Definir una función dentro de otra

def calculadora(a, b, operacion ='sumar'):

    # 1. Función anidada
    def sumar(a, b):
        return a + b
    def restar(a, b):
        return a - b
    def multipl(a, b):
        return a * b

    # 2. Llamar la función anidada
    if operacion == 'sumar':
        print(f' Resultado de sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f' Resultado de restar: {restar(a, b)}')
    elif operacion == 'multiplicar':
        print(f' Resultado de multipl: {multipl(a, b)}')

calculadora(5, 6)
calculadora(5, 6, 'restar')
calculadora(5, 6, 'multiplicar')