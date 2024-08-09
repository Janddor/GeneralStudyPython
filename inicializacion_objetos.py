# Orden de inicialización de objetos
class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('Metodo Padre')

class Hijo(Padre):
    # Si no se agrega un método inicializador, se llamará el de padre automáticamente.

    def __init__(self): # Se sobreescribe el método init, ya no tomará el de padre
        # De manera opcional podemos llamar al metodo __init__ de la clase Padre
        super().__init__() # Por si se quiere llamar el método de padre.
        print('Inicializador Hijo')

    # Sobreescribimos el método heredado de la clase padre
    def metodo(self):
        super().metodo() # Por si se quiere llamar el método de padre.
        print('Método sobreescrito hijo')

# padre1 = Padre()
# padre1.metodo()

hijo1 = Hijo()
hijo1.metodo()