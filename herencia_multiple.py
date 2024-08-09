# Ejemplo de herencia simple
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos = []):
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()

# Lista solo acepta números enteros
class ListaEnteros(ListaSimple):
    def __init__(self, elementos = []):
        for elemento in elementos:
            self._validar(elemento)
        # Si el elemento es válido, se agrega
        super().__init__(elementos)

    def _validar(self, elemento):
        # validar si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f' No es un valor entero: {elemento}')

    # Sobreescribimos el método agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar(elemento)

# Lista enteros ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass



# Lista simple
lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)
# Lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))
# lista de enteros
# lista_enteros = ListaEnteros(['Hola', 1, 2, 3]) # Envía un error por el 'Hola'
lista_enteros = ListaEnteros([1, 3, 4, -15])
print(lista_enteros)

# Lista enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4 ,5, 1 , -4, 14, 10])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)

# Saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
'''
(<class '__main__.ListaEnteros'>, <class '__main__.ListaOrdenada'>)
'''
# MRO (Method Resolution Order)
print(ListaEnterosOrdenada.mro())
'''
[<class '__main__.ListaEnterosOrdenada'>, <class '__main__.ListaEnteros'>, 
<class '__main__.ListaOrdenada'>, <class '__main__.ListaSimple'>, <class 'object'>]
'''
# isinstance true si es parte de una clase, o si es parte de alguna de las clases del MRO
print(f'Es entero? {isinstance(1, int)}') # True
print(f'Es cadena? {isinstance('hola', str)}') # True
print(f'Es lista ent. ord.? {isinstance(lista_enteros_ordenada, ListaEnterosOrdenada)}') # True
print(f'Es lista ent? {isinstance(lista_enteros_ordenada, ListaEnteros)}') # True
print(f'Es lista simple? {isinstance(lista_enteros_ordenada, ListaSimple)}') # True
print(f'Es tipo object? {isinstance(lista_enteros_ordenada, object)}') # True
print(f'Es de varios tipos? {isinstance(lista_enteros_ordenada, (ListaEnteros, ListaSimple))}')