# Simulación de sobrecarga de constructores en python
# otras formas de crear objetos
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None) # Con () se manda a llamar el método init

    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

# ____________Forma convencional de crear objetos
# persona1 = Persona('Juan', 'Perez')

persona_vacio = Persona.crear_persona_vacia()
print(f'Persona vacío:\n\t {persona_vacio}')

persona_con_valores = Persona.crear_persona_con_valores('Karla', 'Gomez')
print(f'Persona con valores:\n\t {persona_con_valores}')