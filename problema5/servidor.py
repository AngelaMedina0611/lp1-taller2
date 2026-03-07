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

# Evita accesos inseguros a rutas (ej: ../../archivo)
# Solo permite usar el nombre del archivo dentro de BASE_DIR
def safe_path(filename):
    return os.path.join(BASE_DIR, os.path.basename(filename))

# Maneja el comando UPLOAD
def handle_upload(conn, filename, size):
    path = safe_path(filename)

    with open(path, "wb") as f:
        received = 0

        # Recibir el archivo en bloques hasta completar el tamaño esperado
        while received < size:
            data = conn.recv(min(BUFFER, size - received))
            if not data:
                break
            f.write(data)
            received += len(data)
 # Enviar checksum al cliente para verificar integridad
    conn.sendall(checksum(path).encode())
