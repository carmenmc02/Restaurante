# Gestor de Restaurante

Programa en Python, con menú en la terminal, para gestionar una noche de servicio en un restaurante: llegan grupos, se les asigna mesa y camarero, se toma el pedido y se cobra la cuenta.

## Funcionalidad original: camareros y propinas

Cada grupo que se sienta se asigna automáticamente al camarero que tenga menos mesas en ese momento.
Al cobrar, se pregunta la propina: la cuenta se suma a las ganancias del restaurante y la propina se suma al camarero que atendió la mesa.

Al salir del programa se muestra un resumen de la noche con las ganancias del restaurante y las propinas de cada camarero. También se pueden consultar en cualquier momento con la opción 6.

## Cómo ejecutarlo

1. Abrir una terminal dentro de la carpeta del proyecto.
2. Escribir:

```
python main.py
```

Al empezar no hay nada cargado: hay que elegir primero la opción 1.

## Orden de uso

1. **Opción 1**: cargar un restaurante.
2. **Opción 2**: cargar los grupos que llegan (así se ocupan mesas).
3. **Opción 3**: tomar el pedido de una mesa.
4. **Opción 4**: cobrar la mesa y dejarla libre.

Las opciones 5, 6 y 7 se pueden usar en cualquier momento (después de cargar un restaurante).

## Menú del programa

1. **Cargar restaurante:** elegir uno de los archivos de `datos/`.
2. **Cargar nuevos grupos:** leer un archivo de `mesas/` y sentar a cada grupo si hay sitio.
3. **Tomar un pedido:** elegir una mesa y apuntar lo que pide cada cliente, validando contra el menú.
4. **Cobrar y liberar una mesa:** pedir la propina, cobrar y dejar la mesa libre.
5. **Ampliar el menú:** añadir un plato nuevo o cambiar el precio de uno existente. Se guarda en el archivo.
6. **Consultar estado:** ver ocupación, mesas con su camarero, menú, camareros con sus propinas y ganancias.
7. **Salir:** guardar el menú y mostrar el resumen de la noche.

## Qué hay en el proyecto

- `main.py`: el programa que se ejecuta. Muestra el menú y habla con el usuario.
- `restaurante.py`: las reglas del restaurante (sentar grupos, asignar camarero, cobrar, ampliar el menú...).
- `gestor_json.py`: lee y guarda los archivos JSON.
- `datos/`: los restaurantes que se pueden cargar. `roto.json` e `incompleto.json` están mal a propósito, para probar que el programa avisa del error sin romperse.
- `mesas/`: los grupos que llegan al restaurante.

## La carpeta `mesas`

Los grupos que llegan al restaurante se leen de un archivo JSON dentro de la carpeta `mesas`, que simula el sistema de recepción de la puerta.

Esta carpeta está en el `.gitignore`, así que **no se descarga con el proyecto**. Hay que crearla a mano:

1. Crear una carpeta llamada `mesas` junto a `main.py`.
2. Dentro, crear un archivo `grupos.json` con, por ejemplo:

```json
[
    {"clientes": 4},
    {"clientes": 2},
    {"clientes": 6}
]
```

## Formato del archivo de un restaurante

```json
{
  "nombre": "Calle 365",
  "capacidad": 50,
  "mesas_max": 5,
  "menu": {
    "Sushi": 32,
    "Sopa": 1,
    "Sancocho": 7
  },
  "camareros": ["Alvaro", "Isaac"]
}
```
- `nombre`: nombre del restaurante.
- `capacidad`: número máximo de personas en el restaurante a la vez.
- `mesas_max`: número máximo de mesas a la vez.
- `menu`: cada plato con su precio.
- `camareros`: nombres de los camareros que trabajan esa noche.

Los cinco campos son obligatorios: si falta alguno, el archivo no se carga y el programa avisa.