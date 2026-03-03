#!/usr/bin/env python3
"""
Problema 1: Sockets básicos - Cliente
Objetivo: Crear un cliente TCP que se conecte a un servidor e intercambie mensajes básicos
"""

import socket

def main():
    # crear sockets Tcp/Ip
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Establece coneción con el servidor
    servidor = ('127.0.0.1', 65432)
    cliente.connect(servidor)
    # Envia datos al servidor
    mensaje = "Hola servidor"
    cliente.sendall(mensaje.encode('utf-8'))
    # recibir respuesta del servidor
    datos = cliente.recv(1024)
    print("Respuesta del servidor:", datos.decode('utf-8'))
    # Cerrar la conexión con el servidor
    cliente.close()

