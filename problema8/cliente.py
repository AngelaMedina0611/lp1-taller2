import socket
import threading

# Dirección del servidor
HOST = "127.0.0.1"
PORT = 5000

def receive(sock):
    """
    Hilo encargado de recibir mensajes del servidor
    para que el cliente pueda escribir y recibir al mismo tiempo.
    """
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print(msg)
        except:
            break
        
def start_client():
    """
    Conecta el cliente al servidor y permite enviar mensajes.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
