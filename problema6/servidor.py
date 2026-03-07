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

# Archivo donde se guardan las salas (persistencia básica)
ROOM_FILE = "rooms.json"

# -----------------------------------------------------------
# CARGAR SALAS DESDE ARCHIVO
# -----------------------------------------------------------
def load_rooms():
    """
    Carga las salas guardadas en el archivo rooms.json.
    Si no existe, crea una sala por defecto llamada 'general'.
    """
    global rooms

    if os.path.exists(ROOM_FILE):
        with open(ROOM_FILE, "r") as f:
            rooms = json.load(f)
    else:
        rooms = {"general": []}
        
def save_rooms():
    """
    Guarda las salas actuales en un archivo JSON.
    Esto permite que las salas no se pierdan al reiniciar el servidor.
    """
    with open(ROOM_FILE, "w") as f:
        json.dump(rooms, f)

