import socket
import threading

# Dirección y puerto del servidor principal
HOST = "127.0.0.1"
PORT = 5000

# Dirección del servidor secundario donde se replicarán los datos
REPLICA_HOST = "127.0.0.1"
REPLICA_PORT = 6000

# Lista para almacenar los mensajes recibidos
messages = []

def replicate(message):
    """
    Envía el mensaje recibido al servidor secundario
    para replicar los datos.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conectarse al servidor secundario
        s.connect((REPLICA_HOST, REPLICA_PORT))
        
        # Enviar el mensaje
        s.sendall(message.encode())