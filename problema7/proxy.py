import socket
import threading

# Dirección y puerto donde el proxy escuchará las conexiones
HOST = "127.0.0.1"
PORT = 8888

# Tamaño del buffer para recibir datos
BUFFER = 4096

def log(msg):
    """
    Función simple para mostrar mensajes de log
    que ayudan a monitorear el funcionamiento del proxy.
    """
    print(f"[PROXY] {msg}")
    
def tunnel(client, host, port):
    """
    Maneja conexiones HTTPS usando el método CONNECT.
    Crea un túnel entre cliente y servidor para reenviar
    datos en ambas direcciones.
    """
     try:
        # Conectar al servidor destino
        server = socket.create_connection((host, port))
        
        # Responder al cliente que el túnel fue establecido
        client.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
        
         # Función que reenvía datos entre sockets
        def forward(source, destination):
            while True:
                data = source.recv(BUFFER)
                if not data:
                    break
                destination.sendall(data)
                
         # Crear dos hilos para reenviar datos en ambas direcciones
        t1 = threading.Thread(target=forward, args=(client, server))
        t2 = threading.Thread(target=forward, args=(server, client))

        t1.start()
        t2.start()
        
         # Esperar a que ambos terminen
        t1.join()
        t2.join()
        
finally:
        # Cerrar conexiones
        client.close()
        server.close()
        
def handle_http(client, request):
    """
    Maneja peticiones HTTP normales.
    Extrae el host del header y reenvía la petición
    al servidor correspondiente.
    """
    lines = request.split(b"\r\n")
    host = None 
    
      # Buscar el header Host
    for line in lines:
        if line.lower().startswith(b"host:"):
            host = line.split(b":", 1)[1].strip().decode()




