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
        
# -----------------------------------------------------------
# ENVIAR MENSAJE A TODOS LOS USUARIOS DE UNA SALA
# -----------------------------------------------------------
def broadcast(room, message, sender=None):
    """
    Envía un mensaje a todos los usuarios de una sala.
    El remitente no recibe su propio mensaje.
    """
    for user in rooms.get(room, []):
        if user != sender and user in clients:
            try:
                clients[user].send(message.encode())
            except:
                pass
# -----------------------------------------------------------
# MENSAJES PRIVADOS
# -----------------------------------------------------------
def private_message(sender, target, message):
    """
    Envía un mensaje privado entre usuarios.
    """
    if target in clients:
        clients[target].send(f"[PRIVADO] {sender}: {message}".encode())
    else:
        clients[sender].send("Usuario no encontrado".encode())
# -----------------------------------------------------------
# CREAR SALA
# -----------------------------------------------------------
def create_room(room, user):
    """
    Crea una nueva sala si no existe.
    """
    with lock:
        if room not in rooms:
            rooms[room] = []
            save_rooms()
            clients[user].send(f"Sala '{room}' creada\n".encode())
        else:
            clients[user].send("La sala ya existe\n".encode())
# -----------------------------------------------------------
# UNIRSE A UNA SALA
# -----------------------------------------------------------
def join_room(room, user):
    """
    Permite a un usuario unirse a una sala existente.
    Si el usuario ya está en otra sala, se le saca de esa sala antes de unirse a la nueva.
    """
    with lock:

        # Verificar si la sala existe
        if room not in rooms:
            clients[user].send("La sala no existe\n".encode())
            return