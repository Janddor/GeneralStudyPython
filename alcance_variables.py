# Alcance de variables (scope)

var_global = 'Variable global'

def imprimir():
    # Definir las variables globales
    global var_global

    # Definición de variable local
    var_local = 'Variable local'

    # Acceder a una variable global
    print(f'Variable global desde función: {var_global}')
    var_global = 'Nuevo valor'
    print(f'Variable local desde función:{var_local}')

    # Función anidada
    def funcion_anidada():
        print(f'Variable local dentro funcion anidada: {var_local}')

    funcion_anidada()

imprimir()
print(f'Var global fuera función: {var_global}')
# print(f'Var local fuera función: {var_local}')