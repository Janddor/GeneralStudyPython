# Leer archivo json
# JSON = JavaScript Object Notation
from urllib.request import Request as req
from urllib.request import urlopen
import json

request = req("http://globalmentoring.com.mx/api/personas.json")
# Añadir la cebecera User-Agent a la peticion
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
respuesta  = urlopen(request)
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
print(json_respuesta)
# Imprimir sólo los nombres de las personas
# JSON se convierte a listas y diccionarios en Python
for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]} {persona["edad"]}')
# Accedemos a las variables independientes
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Mensaje: {json_respuesta["mensaje"]}')