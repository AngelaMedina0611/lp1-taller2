# Problema: Sistema con Múltiples Servidores

Este proyecto implementa un sistema de cliente-servidor con replicación de datos usando sockets en Python.
El sistema utiliza dos servidores que se comunican entre sí para mantener la información sincronizada.

## Archivos del proyecto
servidor1.py  # Servidor principal que recibe clientes
servidor2.py  # Servidor secundario que replica los datos
cliente.py    # Cliente que envía mensajes al servidor
## Funcionamiento

* Servidor 1 recibe mensajes de los clientes.

* Los mensajes se guardan localmente.

* El servidor envía esos mensajes al Servidor 2.

* Servidor 2 replica y almacena los datos recibidos.

* De esta forma ambos servidores mantienen la misma información.

## Ejecución

* Iniciar el servidor secundario:

* python3 servidor2.py

* Iniciar el servidor principal:

* python3 servidor1.py

* Ejecutar el cliente:

* python3 cliente.py
Prueba

*  El cliente puede enviar mensajes como:

* hola
mensaje de prueba

* El Servidor 1 recibirá el mensaje y el Servidor 2 lo replicará automáticamente.

## Conceptos aplicados

* Sockets TCP

* Arquitectura cliente-servidor

* Comunicación entre servidores

* Replicación de datos

* Concurrencia con threading

