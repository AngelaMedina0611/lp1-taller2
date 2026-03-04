#!/usr/bin/env python3
"""
Problema 2: Comunicación bidireccional - Cliente
Objetivo: Crear un cliente TCP que envíe un mensaje al servidor y reciba la misma respuesta
"""

import socket

# Definir la dirección y puerto del servidor
HOST = '127.0.0.1'
PORT = 65432

# Solicitar mensaje al usuario por consola
message = input("Mensaje: ")

# socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor en la dirección y puerto especificados
client.connect((HOST, PORT))

# Mostrar mensaje que se va a enviar
print(f"Mensaje '{message}' enviado.")

# mensaje a bytes y enviarlo al servidor
# sendall() asegura que todos los datos sean enviados
client.sendall(message.encode())


# Recibir datos del servidor (hasta 1024 bytes)
data = client.recv(1024)

# Decodificar e imprimir los datos recibidos
print("Mensaje recibido: ", data.decode())

# Cerrar la conexión con el servidor
client.close()

