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
    
    # Enviar comando con nombre y tamaño del archivo
    sock.sendall(f"UPLOAD {filename} {size}".encode())
    
     # Enviar archivo en bloques
    with open(filename, "rb") as f:
        while chunk := f.read(BUFFER):
            sock.sendall(chunk)
    
     # Recibir checksum calculado por el servidor
    server_hash = sock.recv(1024).decode()


