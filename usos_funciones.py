# Las funciones en python son ciudadanas de primera clase
# First class citizens

# Definimos la función
def sumar(a,b):
    return a + b

# 1. Asignar una función a una variable (no se usan paréntesis)
mi_funcion = sumar

# Verificar el tipo de variable
print(f'Tipo de variable mi_funcion: {type(mi_funcion)}')

# Llamamos la función a través de la variable
resultado = mi_funcion(5, 8)
print(f'Resultado de llamar mi_funcion(5,8): {resultado}')

# 2. Función como argumento
def operacion(a, b, sumar_arg):
    print(f'Resultado de sumar {a} y {b}: {sumar_arg(a, b)}')
operacion(4, 5, sumar)

# 3. Retornar una función
def retornar_funcion():
    return sumar
mi_funcion_retornada = retornar_funcion()
print(f'Resultado de retornar: {mi_funcion_retornada(5, 7)}')