class Persona:
    # Atributo de clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Atributos de instancia u objeto
        self.nombre = nombre
        self.apellido = apellido

# Mostrar los atributos de un objeto
persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__) # Entrega un diccionario con los atributos del objeto

# Crear un atributo al vuelo
persona1.contador_personas = 10 # No se usa el atributo de clase, se crea uno nuevo.
print(persona1.__dict__) # Entrega un diccionario con los atributos del objeto, ahora sumó el atributo nuevo
# El atributo anterior oculta al atributo de clase.
print(f'Atributo de clase: {Persona.contador_personas}') # Sigue en 0, nunca cambió.

# Un segundo objeto
# Solo va a tener nombre y apellido, no tendrá el atributo contador, ya que solo se creó en persona1.
persona2 = Persona('Karla', 'Gomez')
print(persona2.__dict__)
print(f'Atributo de clase: {Persona.contador_personas}') # Sigue en 0, nunca cambió.

# Asociar un atributo de clase al vuelo.
Persona.contador2 = 20
print(f'Atributo de clase al vuelo: {Persona.contador2}') #