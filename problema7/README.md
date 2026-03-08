# Problema 7: Proxy HTTP

## Descripción

Este proyecto implementa un **proxy HTTP básico en Python** que actúa como intermediario entre un cliente y un servidor web. El proxy recibe peticiones del cliente, se conecta al servidor destino y reenvía los datos entre ambos.

También soporta conexiones **HTTPS** utilizando el método `CONNECT`, creando un túnel seguro entre cliente y servidor.

## Conceptos aplicados

* Proxy explícito
* Reenvío de peticiones HTTP
* Manejo del método CONNECT para HTTPS
* Comunicación cliente-servidor con sockets
* Uso de hilos para manejar múltiples conexiones

## Requerimientos implementados

* Recepción de peticiones desde el cliente
* Conexión con el servidor destino
* Reenvío bidireccional de datos
* Manejo de conexiones HTTPS mediante `CONNECT`
* Registro básico de conexiones (logging)

## Ejecución

1. Ejecutar el proxy:

```
python3 proxy.py
```

2. Probar con `curl`.

HTTP:

```
curl -x http://127.0.0.1:8888 http://example.com
```

HTTPS:

```
curl -x http://127.0.0.1:8888 https://example.com
```

## Funcionamiento

1. El proxy escucha conexiones en 127.0.0.1:8888.

2. Un cliente se conecta al proxy y envía una petición HTTP o HTTPS.

3. El proxy analiza la primera línea de la petición:

* Si es HTTP, extrae el host del header y reenvía la petición al servidor.

* Si es HTTPS, usa el método CONNECT para crear un túnel seguro.

4. El proxy reenvía los datos entre cliente y servidor hasta que la conexión termina.

## Ejemplo de salida

```
[PROXY] Proxy escuchando en 127.0.0.1:8888
[PROXY] Cliente conectado ('127.0.0.1', 34094)
[PROXY] GET http://example.com/ HTTP/1.1
[PROXY] CONNECT example.com:443 HTTP/1.1
```

## Estructura

```
problema7/
 ├── proxy.py
 └── README.md
```
