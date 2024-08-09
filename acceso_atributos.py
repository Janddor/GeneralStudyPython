# Ejemplo atributos publicos, protegidos, privados en PYTHON

class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico # Se usará en otras clases si se requiere
        self._protegido = protegido # Se usará solo en esta clase o subclases
        self.__privado = privado # Se usará solo en esta clase

objeto = MiClase('Valor público', 'Valor protegido', 'Valor privado')
# Acceso al atributo público
print(objeto.publico)
# Modificar el valor público
objeto.publico = 'Nuevo valor público'
print(objeto.publico)

# Acceso al valor protegido
# Solo dentro de la misma clase o clases hijas
print(objeto._protegido)
# Modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido' # Esto debería hacerse con sett y get, en la misma clase o hijas.
print(objeto._protegido)

# Acceder al valor privado
# print(objeto.__privado) # No es posible, python protege atributos privados
# Pero, accediendo mediante la clase si es posible. objeto._nombreclase__atributoPrivado
print(objeto._MiClase__privado) # No recomendable
objeto._MiClase__privado = 'Nuevo valor privado' # No recomendable
print(objeto._MiClase__privado) # No recomendable