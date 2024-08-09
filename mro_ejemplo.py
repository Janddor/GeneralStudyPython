class Clase1:
    def __init__(self):
        print(f'Clase1.__init__')

    def metodo(self):
        print('Metodo Clase1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo Clase2')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo Clase3')
        super().metodo()
class Clase4(Clase2, Clase3):
    # Se llamará automaticamente el método init de la clase2 al no especificar un método init
    # def __init__(self):
    #     print('Clase4.__init__')
    def metodo(self):
        print('Metodo Clase4')
        super().metodo()

# Creamos objeto clase4
clase = Clase4()
# __bases__
print(Clase4.__bases__)
'''
(<class '__main__.Clase2'>, <class '__main__.Clase3'>)
'''
# MRO
print(Clase4.mro())
'''
[<class '__main__.Clase4'>, <class '__main__.Clase2'>, <class '__main__.Clase3'>, <class '__main__.Clase1'>, <class 'object'>]
'''
# Cuál método se ejecuta
clase.metodo() # Clase2 si no estuviera definido en Clase4, Si tampoco en Clase2, entonces Clase3, sino, entonces Clase1
