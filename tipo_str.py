# Profundizando en el tipo str
import math
from mi_clase import MiClase

# # Concatenación automática
# variable = 'Adiós'
# mensaje = 'Hola ''Mundo ' + 'Adiós'
# mensaje += ' ''Universidad'' ''Python'
# print(mensaje)

# help(float)
# help(math)
# help(math.isnan)

# help(MiClase)

# print(MiClase.__doc__) #Llama la documentación de la clase
# print(MiClase.mi_metodo.__doc__) #documentación del método
# print(MiClase.mi_metodo)#Imprime dirección del objeto
# print(type(MiClase.mi_metodo))#Imprime tipo del objeto

# Las cadenas son inmutables
# help(str.capitalize)

# mensaje1 = 'hola mundo'
# mensaje2 = mensaje1.capitalize() # Colocar mayus primera letra
# print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
# print(f'mensaje2: {mensaje2}, id: {hex(id(mensaje2))}')
# mensaje1 += 'adios'
# print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
# # con eso ya guarda en una nueva dirección de memoria

# help(str.join)

# tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
# resultado_tupla = ' '.join(tupla_str)
# print(f'mensaje tupla join " ": {resultado_tupla}')
#
# lista_str = ('Java', 'Python', 'Angular', 'Spring')
# resultado_lista = ', '.join(lista_str)
# print(f'mensaje lista join " ": {resultado_lista}')
#
# cadena = 'HolaMundo'
# mensaje = '.'.join(cadena)
# print(mensaje)
#
# diccionario = {'nombre':'Juan', 'apellido':'Perez', 'edad':'18'}
# llaves = ' - '.join(diccionario.keys())
# valores = ' * '.join(diccionario.values())
# print(f'llaves: {llaves}, type: {type(llaves)}')
# print(f'valores: {valores}, type: {type(valores)}')


# # help(str.split) #entrega una lista de substrings de un string
#
# cursos = 'Java Python Javascript Angular Spring Excel'
# lista_cursos = cursos.split() #separar con split por defecto con ' '
# print(f'Lista cursos: {lista_cursos} type: {type(lista_cursos)}')
#
# cursos_csv = 'Java, Python, Javascript, Angular, Spring, Excel'
# lista_cursos = cursos_csv.split(', ')#separar con caracter ', '
# print(f'Lista cursos: {lista_cursos} type: {type(lista_cursos)}')
#
# cursos_csv = 'Java, Python, Javascript, Angular, Spring, Excel'
# lista_cursos = cursos_csv.split(', ',3)#con maxsplit se separan los primeros n elementos.
# print(f'Lista cursos: {lista_cursos} type: {type(lista_cursos)} largo lista: {len(lista_cursos)}')

# # dar formato a un str
# nombre = 'Juan'
# edad = 28
# mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre, edad)
# print(mensaje_con_formato)
#
# persona = ('Karla', 'Gomez', 5000.0)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'%persona
# print(mensaje_con_formato)

# persona = ('Karla', 'Gomez', 5000.0)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
# print(mensaje_con_formato%persona)

# nombre = 'Juan'
# edad = 28
# sueldo = 3000
# mensaje = 'Nombre: {} Edad: {} Sueldo: {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)
#
# mensaje = 'Nombre: {0} Edad: {1} Sueldo: {2:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)
#
# mensaje = 'Sueldo: {2:.2f} Nombre: {0} Edad: {1}'.format(nombre, edad, sueldo)
# print(mensaje)
#
# mensaje = 'Nombre: {n} Edad: {e} Sueldo: {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)
#
# diccionario = {'nombre':'Ivan', 'edad':35, 'sueldo':8000.0}
# mensaje = 'Nombre: {dic[nombre]} Edad: {dic[edad]} Sueldo: {dic[sueldo]:.2f}'.format(dic=diccionario)
# print(mensaje)


# # uso de f-string (Template Literal)
#
# nombre = 'Juan'
# edad = 28
# sueldo = 3000
# mensaje = f'Nombre: {nombre} Edad: {edad} Sueldo {sueldo:.2f}'
# print(mensaje)
#
# # Método print
# print(nombre, edad, sueldo, sep=', ')


# # Multiplicación str
# resultado = 5*'Hola'
# print(f'Resultado: {resultado}')
#
# # Multiplicación de tuplas
# resultado = 5*('Hola',10)
# print(f'Resultado: {resultado}')
#
# # Multiplicación de listas
# resultado = 10*[0]
# print(f'Resultado: {resultado}, largo: {len(resultado)}')



# # Caracteres de escape
# resultado = 'Hola \' Mundo'
# print(f'Resultado: {resultado}')
#
# resultado = 'Se elimina el punto.\b'
# print(f'Resultado: {resultado}')
#
# # Caracter \
# resultado = 'c:\\directorio\\juan'
# print(f'Resultado: {resultado}')
#
# # raw string
# resultado = r'Cadena con \n salto de línea'
# print(f'Resultado: {resultado}')

# # Juego de caracteres Unicode
# print('Hola\u0020Mundo')
# print('Notación simple:','\u0041')
# print('Notación extendida','\U00000041')
# print('Notación hexadecimal','\x41')
#
# print('Corazón:','\u2665')
# print('Cara sonriente:','\U0001F600')
# print('Serpiente:','\U0001F40D')
#
# # Juego de caracteres ASCII
# caracter = chr(65)
# print('A:',caracter)
# caracter = chr(64)
# print('Arroba:',caracter)
# caracter = chr(97)
# print('a:',caracter)

# # Caracteres en byte
# caracteres_en_bytes = b'Hola Mundo'
# print(caracteres_en_bytes)
#
# mensaje = b'Universidad Python'
# print(mensaje[0])
# print(chr(mensaje[0]))
# lista_caracteres = mensaje.split()
# print(lista_caracteres)

# Convertir str a bytes
string = 'Programación con Python'
print('string original: ',string)

bytes = string.encode('UTF-8')
print('bytes codificado:', bytes)

# Convertir de bytes a str
string2 = bytes.decode('UTF-8')
print('string decodificado:',string2)
print(string == string2)
