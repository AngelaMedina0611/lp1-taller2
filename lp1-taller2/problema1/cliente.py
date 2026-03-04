#!/usr/bin/env python3
"""
Problema 1: Sockets básicos - Cliente
Objetivo: Crear un cliente TCP que se conecte a un servidor e intercambie mensajes básicos
"""

import socket

def main():
    print("Iniciando cliente...")

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor = ('127.0.0.1', 65432)

    