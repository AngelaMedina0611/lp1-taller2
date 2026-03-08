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
