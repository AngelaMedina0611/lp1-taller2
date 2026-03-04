#!/usr/bin/env python3
"""
Problema 1: Sockets básicos - Servidor
Objetivo: Crear un servidor TCP que acepte una conexión y intercambie mensajes básicos
"""

import socket
def main():
    # scoket TCP/IP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Asociar la dirección y puerto del servidor
    direccion = ('127.0.0.1', 65432)
    servidor.bind(direccion)
  