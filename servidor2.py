import socket

# Dirección y puerto del servidor secundario
HOST = "127.0.0.1"
PORT = 6000

# Lista para almacenar los mensajes replicados
messages = []

# Crear socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociar el socket al puerto
server.bind((HOST, PORT))

# Escuchar conexiones
server.listen()

print("Servidor 2 escuchando en", PORT)

while True:
    # Esperar conexión del servidor principal
    conn, addr = server.accept()
    
     # Recibir datos
    data = conn.recv(1024)
