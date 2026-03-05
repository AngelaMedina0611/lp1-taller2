#!/usr/bin/env python3
"""
Problema 4: Servidor HTTP básico - Cliente
Objetivo: Crear un cliente HTTP que realice una petición GET a un servidor web local
"""

import http.client

# Definir la dirección y puerto del servidor HTTP
HOST = "localhost"
PORT = 8000

# Crear una conexión HTTP con el servidor
# HTTPConnection permite establecer conexiones HTTP con servidores
connection = http.client.HTTPConnection(HOST, PORT)

# Realizar una petición GET al path raíz ('/')
# request() envía la petición HTTP al servidor
# Primer parámetro: método HTTP (GET, POST, etc.)
# Segundo parámetro: path del recurso solicitado
connection.request("GET", "/")

# Obtener la respuesta del servidor
# getresponse() devuelve un objeto HTTPResponse con los datos de la respuesta
response = connection.getresponse()

# Leer el contenido de la respuesta
# read() devuelve el cuerpo de la respuesta en bytes
data = response.read()

# TODO: Decodificar los datos de bytes a string e imprimirlos
# decode() convierte los bytes a string usando UTF-8 por defecto

# TODO: Cerrar la conexión con el servidor

