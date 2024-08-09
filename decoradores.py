# Decoradores
# Un decorador es una función que recibe una función y regresa
# otra
# Se utiliza para extender funcionalidad
# 1. Función decorador (a)
# 2. Función a decorar (b)
# 3. Función decorada  (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        # La función ha sido decorada, y ahora se va a llamar
        print(f'Antes de función')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        # La función ha sido decorada, y se puede
        # ejecutar un código después de haberla ejecutado
        print(f'Después de función')
        return resultado
    return funcion_decorada_c

# @funcion_decorador_a
# def mostrar_mensaje():
#     print(f'Hola desde función mostrar_mensaje')
# @funcion_decorador_a
# def imprimir():
#     print(f'Hola desde función imprimir')
# mostrar_mensaje()
# imprimir()

@funcion_decorador_a
def sumar(a, b):
    return a + b
resultado = sumar(5,6)
print(f'Resultado suma: {resultado}')
