import os
from gestor_json import listar_archivos, cargar_restaurante

def mostrar_menu():
    print("\n===== GESTOR DEL RESTAURANTE =====")
    print("1. Cargar restaurante")
    print("2. Cargar nuevos grupos")
    print("3. Tomar un pedido")
    print("4. Cobrar y liberar una mesa")
    print("5. Ampliar el menú")
    print("6. Consultar estado")
    print("7. Salir")

def pedir_numero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            return int(texto)
        except ValueError:
            print("Eso no es un número, prueba nuevamente.")

def main():
    restaurante = None
    ruta_restaurante = None

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "1":
            ruta = elegir_archivo("datos")
            if ruta is not None:
                nuevo = cargar_restaurante(ruta)
                if nuevo is not None:
                    restaurante = nuevo
                    ruta_restaurante = ruta
                    print(f"Restaurante '{restaurante['nombre']}' cargado.")

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        elif opcion in ["2", "3", "4", "5", "6"]:
            if restaurante is None:
                print("Primero tienes que cargar un restaurante (opción 1).")
            else:
                print("Pendiente.")

        else:
            print("Opción no válida.")

def elegir_archivo(carpeta):
    archivos = listar_archivos(carpeta)
    if len(archivos) == 0:
        print(f"No hay archivos en la carpeta {carpeta}.")
        return None

    print("Archivos disponibles:")
    for i in range(len(archivos)):
        print(f"  {i + 1}. {archivos[i]}")

    while True:
        numero = pedir_numero("Elige un número: ")
        if 1 <= numero <= len(archivos):
            return os.path.join(carpeta, archivos[numero - 1])
        print("Ese número no está en la lista.")

if __name__ == "__main__":
    main()