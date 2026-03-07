import socket
import threading
import json
import os

# Dirección y puerto del servidor
HOST = "127.0.0.1"
PORT = 5001

# Diccionario de clientes conectados -> {usuario : socket}
clients = {}

# Diccionario que guarda en qué sala está cada usuario -> {usuario : sala}
user_rooms = {}

# Diccionario de salas -> {sala : [usuarios]}
rooms = {}

# Lock para evitar problemas de concurrencia entre hilos
lock = threading.Lock()

# Archivo donde se guardarán las salas (persistencia básica)
ROOM_FILE = "rooms.json"
