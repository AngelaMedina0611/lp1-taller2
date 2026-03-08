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