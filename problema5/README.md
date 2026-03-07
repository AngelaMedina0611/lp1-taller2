# Problema 5: Transferencia de Archivos (Upload/Download)
## Conceptos clave

- Manejo de datos binarios: permite transferir archivos de cualquier tipo (texto, imágenes, etc.).

- Protocolo custom para transferencia de archivos: comunicación entre cliente y servidor mediante comandos definidos.

- Control de flujo y buffers: uso de buffers para transferir archivos grandes de manera eficiente.

- Comandos del sistema:

- UPLOAD: subir un archivo al servidor.

- DOWNLOAD: descargar un archivo desde el servidor.

- LIST: listar los archivos disponibles.

## Requerimientos

- Implementar protocolo de comandos entre cliente y servidor para gestionar las operaciones de archivos.

- Manejar archivos grandes utilizando buffers, evitando cargar todo el archivo en memoria.

- Validar la integridad de los archivos mediante un checksum.

- Implementar manejo seguro de rutas de archivos para evitar accesos no autorizados en el sistema.

## Funcionamiento general

- El sistema sigue una arquitectura cliente-servidor:

- El servidor escucha conexiones entrantes.

- El cliente se conecta al servidor y envía comandos.

- El servidor procesa el comando recibido y realiza la operación correspondiente sobre los archivos.

- Los datos se transmiten en bloques (buffers) para mejorar el rendimiento y soportar archivos grandes.

- Comandos disponibles

## Ejemplos de uso desde el cliente:

UPLOAD archivo.txt
DOWNLOAD archivo.txt
LIST

Estos comandos permiten gestionar los archivos almacenados en el servidor.

## Autor

Angela Maria Medina Ruiz