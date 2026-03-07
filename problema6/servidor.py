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
