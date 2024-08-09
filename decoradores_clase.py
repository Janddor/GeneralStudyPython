# Decoradores de Clase
# Similares a los decoradores de funciones. (metaprogramación)
# Permiten programar de manera programática nuestra clase
import inspect

def decorador_repr(cls):
    print('Se ejecuta el decorador decorador_repr')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo del diccionario
    # for nombre, atributo in atributos.items():
    #     print(nombre, atributo)

    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')
    firma_init = inspect.signature(cls.__init__)
    print(f'Firma del método __init__:{firma_init}')
    # Recuperamos los parámetros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros init: {parametros_init}')

    # Revisar si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # property es un valor tipo built-in para preguntar si se está usando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un metodo property para el parámetro: {parametro}')


    # Crear el método repr dinámicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase dinámicamente
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')

        # Obtenemos los nombres de las propiedades y sus valores
        # Expresión generadora para crear: nombre_atr = valor_atr
        generador_argumentos = (f'{nombre}={getattr(self, nombre)!r}' #Yield
                                for nombre in parametros_init) #for
        # Lista de argumentos del generador
        lista_arg = list(generador_argumentos)
        print(f'Lista del generador: {lista_arg}')
        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del método repr: {argumentos} ')
        # Creamos la forma del método __repr__, sin su nombre
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        # print(f'Resultado del método rpr: {resultado_metodo_repr}')
        return resultado_metodo_repr
    # Agregar dinámicamente el método repr a nuestra clase
    setattr(cls,'__repr__', metodo_repr)


    return cls
@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('Se ejecuta el inicializador de Persona()')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # def __repr__(self):
    #     return f'Persona({self.nombre}, {self.apellido})'

persona1 = Persona('Juan', 'Perez', 28)
print()
print(persona1)
persona2 = Persona('Karla', 'Gomez', 30)
print()
print(persona2)
print()
# Tiene los métodos de propiedad nombre, apellido, repr
print(dir(Persona))
# Tiene el método repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)