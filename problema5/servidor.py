import socket
import os
import hashlib

# Configuración del servidor
HOST = "127.0.0.1"
PORT = 5000
BUFFER = 4096

# Carpeta donde se almacenarán los archivos del servidor
BASE_DIR = "server_files"
os.makedirs(BASE_DIR, exist_ok=True)  # Crear carpeta si no existe