import socket
import threading

# Dirección y puerto del servidor principal
HOST = "127.0.0.1"
PORT = 5000

# Dirección del servidor secundario donde se replicarán los datos
REPLICA_HOST = "127.0.0.1"
REPLICA_PORT = 6000

# Lista para almacenar los mensajes recibidos
messages = []

def replicate(message):
    """
    Envía el mensaje recibido al servidor secundario
    para replicar los datos.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conectarse al servidor secundario
        s.connect((REPLICA_HOST, REPLICA_PORT))
        
        # Enviar el mensaje
        s.sendall(message.encode())
        
         # Cerrar conexión
        s.close()

    except:
        print("No se pudo replicar el mensaje")
        
def handle_client(conn, addr):
    """
    Maneja la comunicación con cada cliente conectado.
    Cada cliente se ejecuta en un hilo independiente.
    """
    print("Cliente conectado:", addr)
    
    while True:
        try:
            # Recibir datos del cliente
            data = conn.recv(1024)
            
             # Si no hay datos, el cliente se desconecta
            if not data:
                break
            
            # Convertir los datos a texto
            msg = data.decode()
            
            print("Mensaje recibido:", msg)

            # Guardar mensaje en la lista local
            messages.append(msg)
            
            # Replicar el mensaje al servidor secundario
            replicate(msg)

        except:
            break
        
# Cerrar conexión del cliente
    conn.close()

def start_server():
    """
    Inicia el servidor principal y espera conexiones
    de clientes.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Asociar el socket con la dirección y puerto
    server.bind((HOST, PORT))
    
    # Escuchar conexiones entrantes
    server.listen()