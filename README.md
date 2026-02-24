# Aplicación Web Cliente/Servidor para Servicio de Ordenamiento implementada en ASGI

## Descripción

Aplicación web de tipo **Cliente/Servidor** que ofrece como servicio el **ordenamiento de una lista de valores de tipo flotante**. La aplicación está implementada en Python utilizando el estándar **ASGI** (Asynchronous Server Gateway Interface) con el paquete `asgiref` y el servidor `uvicorn`.

## Algoritmos Implementados

### Merge (Fusionar)
Corutina que fusiona dos sublistas ordenadas en una sola lista ordenada. Recibe los mismos parámetros que se especifican en el algoritmo clásico de Merge.

### Merge-Sort (Ordenamiento por Fusión)
Corutina que implementa el algoritmo de ordenamiento recursivo Merge-Sort. Recibe los mismos parámetros que se especifican en el algoritmo clásico. Su comportamiento es el siguiente:

- Las **dos llamadas recursivas a Merge-Sort** se ejecutan de forma **concurrente** (como tareas asíncronas).
- La **llamada a Merge** se ejecuta de manera **normal** (como corutina, de forma secuencial tras las dos tareas).

## Comportamiento de la Aplicación Web

### Petición GET
Cuando el servidor recibe una petición `GET`, envía al cliente un **formulario web** que le permite ingresar una cadena de texto con los elementos a ordenar (valores flotantes separados por comas).

### Petición POST
Cuando el servidor recibe una petición `POST`:
1. Muestra nuevamente el formulario web para ingresar elementos.
2. Recibe la cadena de texto con los elementos enviados por el cliente.
3. Transforma la cadena a una **lista de valores flotantes**.
4. Pasa la lista a la corutina **Merge-Sort** para ordenarla de forma asíncrona y concurrente.
5. Construye una nueva cadena con los elementos **ordenados y separados por comas**.
6. Devuelve al cliente el formulario junto con el resultado del ordenamiento.

## Tecnologías Utilizadas

| Tecnología | Descripción |
|---|---|
| `Python` | Lenguaje de programación principal |
| `asgiref` | Paquete para implementar la interfaz ASGI |
| `uvicorn` | Servidor ASGI de alto rendimiento |
| `asyncio` | Manejo de concurrencia y corutinas |

## Ejecución

```bash
uvicorn server:app --reload
```

Luego abrir el navegador en `http://127.0.0.1:8000`.
