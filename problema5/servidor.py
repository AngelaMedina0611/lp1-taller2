import socket
import os
import hashlib

# Configuración del servidor
HOST = "127.0.0.1"
PORT = 5000
BUFFER = 4096

# Carpeta donde se almacenarán los archivos del servidor
BASE_DIR = "server_files"
os.makedirs(BASE_DIR, exist_ok=True)  # Crear carpeta si no exist

# Calcula el checksum SHA256 de un archivo para verificar integridad
def checksum(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(BUFFER):  # Leer en bloques para soportar archivos grandes
            h.update(chunk)
    return h.hexdigest()
