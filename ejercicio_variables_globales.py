# Definir variable global
contador = 0

def mostrar_contador():
    print(contador)

def modificar_contador(c):
    global contador # Si no se pone global, al usarla se creará una variable local.
    contador = c

modificar_contador(5)
mostrar_contador()