# Leer contenido online

from urllib.request import Request
from urllib.request import urlopen

request = Request("http://globalmentoring.com.mx/recursos/GlobalMentoring.txt")
# Añadir la cebecera User-Agent a la peticion
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
respuesta = urlopen(request)

contenido = respuesta.read().decode('utf-8')
# print(contenido)

# Contar ocurrencias de una cadena dentro de otra
# print('No. de veces "Universidad": ',contenido.count('Universidad'))

# Lower convierte a mayúsculas una str
# print(contenido.upper())# Convierte todo a mayúsculas
# print(contenido)
#
# Lower convierte a minúsculas una str
# print(contenido.lower())# Convierte todo a mayúsculas

# buscar si python existe en un str
# print('Existe python dentro del archivo?: ','python'.lower() in contenido.lower())
# print('Existe python dentro del archivo?: ','python'.upper() in contenido.upper())

# startswith - inicia con
# print(contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - termina con
# print(contenido.lower().endswith('GlobalMentoring.com.mx'.lower()))


# mensaje = 'Hola Mundo'
# print(mensaje.lower().islower()) # Consulta si todos los caracteres están en minus.
# print(mensaje.upper().isupper()) # Consulta si todos los caracteres están en mayus.

#Alinear cadenas

# center = Centrar un str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
# print(titulo.center(50,'*'))
# print(len(titulo.center(50,'*')))
# print(titulo.center(len(titulo)+10,'='))
# print(titulo.ljust(len(titulo)+10,'=')) # Justifica a la izq
# print(titulo.rjust(len(titulo)+10,'=')) # Justifica a la der

# Reemplazar contenido en un str
print(contenido.replace(' ','-'))

# Eliminar caracteres al inicio y al final de un str - stirp
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:',titulo,len(titulo))
titulo = titulo.strip()
print('Cadena modificada:',titulo,len(titulo))
titulo = titulo.strip('*')
print('Cadena modificada:',titulo,len(titulo)) #strip ambos lados los *

titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:',titulo,len(titulo)) #strip ambos lados los *
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:',titulo,len(titulo)) #strip ambos lados los *

#strip multiple
titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena original:',titulo)





