# Problema 6: Chat con Salas
## Descripción

Se implementó un sistema de chat cliente-servidor en Python que permite la comunicación entre múltiples usuarios mediante salas de chat. El servidor administra las conexiones de los clientes, las salas disponibles y el envío de mensajes entre usuarios.

El sistema utiliza sockets para la comunicación en red y threading para manejar múltiples clientes simultáneamente.

## Funcionalidades

- Creación de salas de chat (CREATE)

- Unirse a una sala (JOIN)

- Salir de una sala (LEAVE)

- Listar usuarios dentro de una sala (USERS)

- Enviar mensajes a todos los usuarios de la sala

- Enviar mensajes privados entre usuarios (MSG)

- Persistencia básica de salas usando archivo rooms.json

- Manejo concurrente de múltiples clientes con hilos

## Estructura del proyecto
problema6/
│
├── server.py
├── client.py
└── rooms.json

- server.py → Maneja las conexiones, salas y mensajes.

- client.py → Permite a los usuarios conectarse y enviar mensajes.

- rooms.json → Guarda las salas creadas para mantener persistencia.

## Ejecución
1. Iniciar el servidor
python server.py
2. Ejecutar un cliente
python client.py

Se pueden abrir varias terminales para simular múltiples usuarios.

- Comandos disponibles

- Crear una sala

- CREATE sala1

- Unirse a una sala

- JOIN sala1

- Salir de la sala

- LEAVE

- Ver usuarios en la sala

- USERS

- Enviar mensaje privado

- MSG usuario mensaje
Tecnologías utilizadas

- Python

- Socket Programming

- Threading

- JSON para persistencia de datos