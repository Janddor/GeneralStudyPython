# Funciones lambda
# Son funciones anónimas, y son pequeñas (una línea de código)

# No es posible asignar una función a una variable en su definición:
## mi_funcion = def sumar(a, b): return a + b

# Con una función lambda (anónima, sin nombre, y una sola línea de código
# No se necesita agregar paréntesis para los parámetros
# No se necesita palabra return, pero si debe regresar una expresión válida
mi_funcion_lambda = lambda a, b: a + b
resultado = mi_funcion_lambda(5,6)
print(f'Resultado sumar con mi_funcion_lambda: {resultado}')

# Función lambda que no recibe argumentos (pero debe regresar una expresión válida)
mi_funcion_lambda = lambda: 'Función sin argumentos'
print(f'Llamar función lambda sin argumentos: {mi_funcion_lambda()}')

# Función lambda con parámetros por default
mi_funcion_lambda = lambda a=2, b=3 : a + b
resultado = mi_funcion_lambda()
print(f'Resultado sumar con mi_funcion_lambda con argumentos por def: {resultado}')

# Función lambda con parámetros variables *args o **kwargs
mi_funcion_lambda = lambda *args, **kwargs : len(args) + len(kwargs)
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=5, b=5)}')

# Funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado función lambda: {mi_funcion_lambda(1,2, 3, 5, 6, 7, e = 5, g = 7)}')

