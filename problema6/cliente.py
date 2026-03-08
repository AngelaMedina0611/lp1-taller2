import socket
import threading

# Dirección del servidor
HOST = "127.0.0.1"
PORT = 5001

def receive_messages(sock):
    """
    Hilo que recibe mensajes del servidor continuamente
    para no bloquear la escritura del usuario.
    """
    while True:
        try:
            message = sock.recv(1024).decode()
            print(message)
        except:
            break
