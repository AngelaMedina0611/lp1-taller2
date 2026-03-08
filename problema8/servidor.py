import socket
import threading

# Dirección y puerto del servidor
HOST = "127.0.0.1"
PORT = 5000

# Estado compartido del tablero (9 posiciones)
board = [" " for _ in range(9)]

# Listas de jugadores y espectadores
players = []
spectators = []

# Símbolos de los jugadores
symbols = ["X", "O"]

# Variable que controla el turno actual
current_turn = 0

# Lock para evitar conflictos entre hilos
lock = threading.Lock()

def board_text():
    """
    Convierte el tablero en texto para enviarlo a los clientes.
    """
    b = board
    return f"""
 {b[0]} | {b[1]} | {b[2]}
---+---+---
 {b[3]} | {b[4]} | {b[5]}
---+---+---
 {b[6]} | {b[7]} | {b[8]}
"""
def broadcast(msg):
    """
    Envía un mensaje a todos los jugadores y espectadores.
    """
    for client in players + spectators:
        try:
            client.sendall((msg + "\n").encode())
        except:
            pass

def check_winner():
    """
    Verifica si existe un ganador o empate.
    """
    wins = [
        (0,1,2),(3,4,5),(6,7,8),  # filas
        (0,3,6),(1,4,7),(2,5,8),  # columnas
        (0,4,8),(2,4,6)           # diagonales
    ]
    
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    # Si no hay espacios vacíos y nadie ganó, es empate
    if " " not in board:
        return "Empate"

    return None

def handle_client(conn):
    """
    Maneja la conexión de cada cliente en un hilo independiente.
    """
    global current_turn
    
     # Mensaje inicial al conectarse
    conn.send("JOIN para jugar | WATCH para observar\n".encode())
    
    role = conn.recv(1024).decode().strip().upper()

    # Sección crítica para modificar listas compartidas
    with lock:
         # Matchmaking: solo 2 jugadores
        if role == "JOIN" and len(players) < 2:
            players.append(conn)
            symbol = symbols[len(players)-1]
            conn.send(f"Eres jugador {symbol}\n".encode())

        else:
            spectators.append(conn)
            conn.send("Eres espectador\n".encode())

    
