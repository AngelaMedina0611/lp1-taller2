# Problema 8: Servidor de Juegos (Tic-Tac-Toe)

Servidor multijugador de **Tic-Tac-Toe** implementado en Python utilizando **sockets** y **hilos**.
Permite que dos jugadores participen en la partida mientras otros clientes pueden conectarse como espectadores.

## Conceptos implementados

* Estado compartido del tablero
* Coordinación de turnos entre jugadores
* Matchmaking para asignar jugadores
* Validación de movimientos
* Sistema de espectadores
* Notificación de eventos del juego

## Estructura del proyecto

```
problema8/
│
├── servidor.py   # Servidor del juego
└── cliente.py    # Cliente para conectarse al servidor
```

## Ejecución

### 1. Iniciar el servidor

En una terminal ejecutar:

```
python3 servidor.py
```

El servidor quedará escuchando en:

```
127.0.0.1:5000
```

### 2. Conectar clientes

Abrir una o más terminales y ejecutar:

```
python3 cliente.py
```

Al conectarse el cliente deberá elegir:

```
JOIN  -> entrar como jugador
WATCH -> entrar como espectador
```

Solo **dos clientes pueden ser jugadores**.
Los demás se conectarán como **espectadores**.

## Movimientos

Los jugadores deben enviar un número del **0 al 8** correspondiente a la posición del tablero:

```
0 | 1 | 2
3 | 4 | 5
6 | 7 | 8
```

El servidor valida que:

* Sea el turno correcto
* La posición esté dentro del tablero
* La casilla esté libre

Después de cada movimiento el servidor envía el tablero actualizado a todos los clientes.

## Funcionamiento

* El servidor mantiene el **estado compartido del tablero**.
* Los clientes se conectan mediante **TCP sockets**.
* Cada cliente es atendido en un **hilo independiente**.
* El servidor controla los **turnos**, valida movimientos y determina **ganador o empate**.
* Jugadores y espectadores reciben **notificaciones del juego en tiempo real**.


