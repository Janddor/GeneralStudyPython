# Leer archivo json
# JSON = JavaScript Object Notation
from urllib.request import Request as req
from urllib.request import urlopen
import json

request = req("http://globalmentoring.com.mx/api/clima.json")
# Añadir la cebecera User-Agent a la peticion
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
respuesta  = urlopen(request)
# print(respuesta)
cuerpo_respuesta = respuesta.read()
# print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
# print(json_respuesta)

# JSON se convierte a listas y diccionarios en Python
# 1. Acceder a la descripcion del clima
# descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')
descripcion_clima = json_respuesta['clima'][0]['descripcion']
print(f'Descripción clima: {descripcion_clima}')

temp_min = json_respuesta.get('principal').get('temp_min')
print(f'Temperatura mínima: {temp_min}')

temp_max = json_respuesta.get('principal').get('temp_max')
print(f'Temperatura máxima: {temp_max}')