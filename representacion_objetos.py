# Hasta el momento lo hemos hecho sobreescribiendo el método str
# Representación de objetos 'dunder'(str, repr, format)
# print(dir(object))

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # repr, más enfocado a los programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre={self.nombre}, apellido={self.apellido})'
    # str es más para el usuario final u otros sistemas
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'
    # format su implementación por default es str
    # se manda a llamar al usar f-string
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Juan', 'Perez')
# repr
print(f'Mi objeto persona1: {persona1!r}') # con !r se llama repr
# str (el método print llama a str por defecto)
print(persona1)# Eso llama al método repr automáticamente si str no está definido. tambien se puede person1.__str__
# format (f'') (Este llama por defecto a str)
print(f'{persona1}')
# print(persona1.__format__(persona1))