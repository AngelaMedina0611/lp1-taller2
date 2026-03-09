import socket

# Dirección del servidor principal
HOST = "127.0.0.1"
PORT = 5000

# Crear socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
client.connect((HOST, PORT))

print("Conectado al servidor")
