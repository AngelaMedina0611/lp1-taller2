#!/usr/bin/env python3
"""
Problema 2: Comunicación bidireccional - Servidor
Objetivo: Crear un servidor TCP que devuelva exactamente lo que recibe del cliente
"""

import socket

# Definir la dirección y puerto del servidor
HOST = '127.0.0.1'
PORT = 65432

# Crear un socket TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección y puerto especificados
server.bind((HOST, PORT))

# Poner el socket en modo escucha
# El parámetro define el número máximo de conexiones en cola
server.listen(1)

# Bucle infinito para manejar múltiples conexiones (una a la vez)
while True:

    print("Servidor a la espera de conexiones ...")
    
    # Aceptar una conexión entrante
    # accept() bloquea hasta que llega una conexión
    # conn: nuevo socket para comunicarse con el cliente
    # addr: dirección y puerto del cliente
    conn, addr = server.accept()
    
    print(f"Conexión realizada por {addr}")

    # Recibir datos del cliente (hasta 1024 bytes)
    data = conn.recv(1024)
    
    # Si no se reciben datos, salir del bucle
    if not data:
        break

    # Mostrar los datos recibidos (en formato bytes)
    print("Datos recibidos:", data)
    
    # Enviar los mismos datos de vuelta al cliente (echo)
    conn.sendall(data)
    
    # TODO: Cerrar la conexión con el cliente actual

