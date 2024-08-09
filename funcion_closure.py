# Función que encapsula otra función, similar a las anidadas pero conserva estados de variables
# closure

# # Funcion principal o externa
# def operacion(a, b):
#     # Definimos una función interna o anidada
#     def sumar():
#         return a + b
#
#     # Retornar la función
#     return sumar
# mi_funcion_closure = operacion(1, 2)
# print(f'Resultado de la función closure: {mi_funcion_closure()}')
#
# # Llamar la función regresada de una vez
# print(f'Resultado de la función closure en linea: {operacion(2,3)()}')

# Closure utilizando funciones lambda
def operacion(a, b):
    # 1. Definir una funcion lambda interna o anidada y se retorna
    return lambda: a + b

print(f'Resultado de la función closure con lambda: {operacion(2,3)()}')