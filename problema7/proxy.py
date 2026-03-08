import socket
import threading

# Dirección y puerto donde el proxy escuchará las conexiones
HOST = "127.0.0.1"
PORT = 8888

# Tamaño del buffer para recibir datos
BUFFER = 4096

def log(msg):
    """
    Función simple para mostrar mensajes de log
    que ayudan a monitorear el funcionamiento del proxy.
    """
    print(f"[PROXY] {msg}")