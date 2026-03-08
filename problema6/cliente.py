import socket
import threading

# Dirección del servidor
HOST = "127.0.0.1"
PORT = 5001

def receive_messages(sock):
    """
    Hilo que recibe mensajes del servidor continuamente
    para no bloquear la escritura del usuario.
    """
    while True:
        try:
            message = sock.recv(1024).decode()
            print(message)
        except:
            break

def main():

    # Crear socket cliente
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
     # Conectarse al servidor
    client.connect((HOST, PORT))
    
     # Crear hilo para recibir mensajes
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.daemon = True
    thread.start()
    
    # Enviar mensajes al servidor
    while True:
        msg = input()
        client.send(msg.encode())
