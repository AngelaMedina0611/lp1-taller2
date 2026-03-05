#!/usr/bin/env python3
"""
Problema 3: Chat simple con múltiples clientes - Cliente
Objetivo: Crear un cliente de chat que se conecte a un servidor y permita enviar/recibir mensajes en tiempo real
"""

import socket
import threading

# Dirección y puerto del servidor
HOST = "127.0.0.1"   # localhost
PORT = 5000          # Puerto donde escucha el servidor

def receive_messages():
    """
    Función ejecutada en un hilo separado para recibir mensajes del servidor
    de forma continua sin bloquear el hilo principal.
    """
    while True:
        try:
            # Recibir mensajes del servidor (hasta 1024 bytes) y decodificarlos
            message = client_socket.recv(1024).decode()

            # Si no se recibe nada, el servidor cierra la conexión
            if not message:
                    print("Conexión cerrada por el servidor.")
                    break

            # Imprimir el mensaje recibido
            print("\n" + message)
        except:
            print("Error al recibir mensaje.")
            client_socket.close()
            break

# Solicitar nombre de usuario al cliente
client_name = input("Cuál es tu nombre? ")

# Crear un socket TCP/IP
# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor en la dirección y puerto especificados
client_socket.connect((HOST, PORT))

# Enviar el nombre del cliente al servidor (codificado a bytes)
client_socket.send(client_name.encode())

# Crear y iniciar un hilo para recibir mensajes del servidor
# target: función que se ejecutará en el hilo
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Bucle principal en el hilo principal para enviar mensajes al servidor
while True:
    try:
    # Solicitar mensaje al usuario por consola
        message = input("Mensaje: ")
     # Codificar el mensaje a bytes y enviarlo al servidor
        client_socket.send(message.encode())
    except:
        print("Error al enviar mensaje.")
        client_socket.close()
        break