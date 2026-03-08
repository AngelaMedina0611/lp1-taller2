import socket
import threading

# Dirección y puerto donde el proxy escuchará las conexiones
HOST = "127.0.0.1"
PORT = 8888

# Tamaño del buffer para recibir datos
BUFFER = 4096