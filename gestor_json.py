import json
import os


def cargar_restaurante(ruta):
    if not os.path.exists(ruta):
        print("No existe el archivo del restaurante")
        return None

    archivo = open(ruta, encoding="utf-8")
    try:
        datos = json.load(archivo)
    except:
        print("El archivo del restaurante está mal escrito")
        archivo.close()
        return None
    archivo.close()

    if "nombre" not in datos or "capacidad" not in datos or "mesas_max" not in datos or "menu" not in datos:
        print("Al archivo del restaurante le faltan campos")
        return None

    restaurante = {
        "nombre": datos["nombre"],
        "capacidad": datos["capacidad"],
        "mesas_max": datos["mesas_max"],
        "menu": datos["menu"],
        "mesas": [],
        "ocupacion": 0,
        "ganancias": 0,
        "siguiente_mesa": 1,
    }
    return restaurante


def cargar_grupos(ruta):
    if not os.path.exists(ruta):
        print("No existe el archivo de grupos")
        return None

    archivo = open(ruta, encoding="utf-8")
    try:
        grupos = json.load(archivo)
    except:
        print("El archivo de grupos está mal escrito")
        archivo.close()
        return None
    archivo.close()
    return grupos


def guardar_menu(ruta, restaurante):
    datos = {
        "nombre": restaurante["nombre"],
        "capacidad": restaurante["capacidad"],
        "mesas_max": restaurante["mesas_max"],
        "menu": restaurante["menu"],
    }
    archivo = open(ruta, "w", encoding="utf-8")
    json.dump(datos, archivo, ensure_ascii=False, indent=4)
    archivo.close()