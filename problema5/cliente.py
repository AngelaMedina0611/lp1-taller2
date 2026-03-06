import socket
import os
import hashlib

# Configuración del cliente
HOST = "127.0.0.1"
PORT = 5000
BUFFER = 4096

# Calcula checksum SHA256 del archivo local
# Se usa para verificar que el archivo enviado o recibido no se corrompió
def checksum(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(BUFFER):
            h.update(chunk)
    return h.hexdigest()

# Enviar archivo al servidor
def upload(sock, filename):
    size = os.path.getsize(filename)

