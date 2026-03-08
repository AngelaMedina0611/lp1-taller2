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
# SALIR DE UNA SALA
# -----------------------------------------------------------
def leave_room(room, user):
    """
    Permite a un usuario salir de una sala.
    """
    with lock:
        if room in rooms and user in rooms[room]:
            rooms[room].remove(user)
            save_rooms()
            if user in user_rooms:
                del user_rooms[user]

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
        
         # Si el usuario está en una sala, salir de ella
        if user in user_rooms:
            leave_room(user_rooms[user], user)
            
         # Agregar usuario a la sala
        rooms[room].append(user)
        
        # Registrar la sala actual del usuario
        user_rooms[user] = room
        
        # Avisar a la sala
        broadcast(room, f"{user} se unió a la sala\n", user)

        clients[user].send(f"Te uniste a la sala {room}\n".encode())
# -----------------------------------------------------------
# SALIR DE UNA SALA
# -----------------------------------------------------------
def leave_room(room, user):
    """
    Elimina a un usuario de una sala.
    """
    with lock:
        if room in rooms and user in rooms[room]:
            rooms[room].remove(user)
            
            # Avisar al resto de usuarios
            broadcast(room, f"{user} salió de la sala\n")
            
             # Eliminar registro de sala del usuario
            del user_rooms[user]
# -----------------------------------------------------------
# LISTAR USUARIOS DE UNA SALA
# -----------------------------------------------------------
def list_users(room, user):
     """
    Envía al usuario la lista de personas conectadas en su sala.
    """
     if room in rooms:
        users = ", ".join(rooms[room])
        clients[user].send(f"Usuarios en {room}: {users}\n".encode())
# -----------------------------------------------------------
# MANEJO DE CADA CLIENTE
# -----------------------------------------------------------
def handle_client(conn, addr):
    """
    Función que maneja la comunicación con cada cliente.
    Cada cliente se ejecuta en un hilo diferente.
    """

    try:
        # Pedir nombre de usuario
        conn.send("Ingresa tu nombre: ".encode())
        username = conn.recv(1024).decode().strip()
        
        # Registrar cliente
        with lock:
            clients[username] = conn

        conn.send(
            "Comandos disponibles:\n"
            "CREATE sala\n"
            "JOIN sala\n"
            "LEAVE\n"
            "USERS\n"
            "MSG usuario mensaje\n".encode()
        )
        while True:

            # Recibir mensaje del cliente
            msg = conn.recv(1024).decode()

            if not msg:
                break

            parts = msg.split()
            # ---------------- COMANDO CREATE ----------------
            if parts[0] == "CREATE":
                create_room(parts[1], username)


    except:
        conn.close()



