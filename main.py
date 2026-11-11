import os
from gestor_json import listar_archivos, cargar_restaurante, guardar_menu, cargar_grupos
from restaurante import añadir_mesa, tomar_pedido, ampliar_menu, mesas_atendidas, cobrar_mesa

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

def cargar_nuevos_grupos(restaurante):
    ruta = elegir_archivo("mesas")
    if ruta is None:
        return

    grupos = cargar_grupos(ruta)
    if grupos is None:
        return

    for grupo in grupos:
        if "clientes" in grupo:
            añadir_mesa(restaurante, grupo["clientes"])
        else:
            print("Hay un grupo sin número de clientes, se ignora.")

def tomar_un_pedido(restaurante):
    while True:
        pendientes = []
        for mesa in restaurante['mesas']:
            if not mesa['atendida']:
                pendientes.append(mesa)

        if len(pendientes) == 0:
            print("No hay mesas esperando pedido.")
            return

        print("Mesas esperando pedido:")
        for mesa in pendientes:
            print(f"  Mesa {mesa['num_mesa']} ({mesa['clientes']} clientes)")

        numero = pedir_numero("¿Qué mesa quieres atender? ")
        elegida = None
        for mesa in pendientes:
            if mesa['num_mesa'] == numero:
                elegida = mesa

        if elegida is None:
            print("Esa mesa no está en la lista.")
        else:
            print("Escribe los platos. Cuando un cliente termine, escribe: Eso es todo")
            tomar_pedido(elegida, restaurante['menu'])
            print(f"Pedido de la mesa {numero} tomado.")

        otra = input("¿Atender otra mesa? (s/n): ").strip().lower()
        while otra != "s" and otra != "n":
            otra = input("Responde s o n: ").strip().lower()
        if otra == "n":
            return

def cobrar_una_mesa(restaurante):
    atendidas = mesas_atendidas(restaurante)
    if len(atendidas) == 0:
        print("No hay mesas para cobrar.")
        return

    print("Mesas listas para cobrar:")
    for mesa in atendidas:
        print(f"  Mesa {mesa['num_mesa']} (camarero: {mesa['camarero']})")

    numero = pedir_numero("¿Qué mesa quieres cobrar? ")

    propina = -1
    while propina < 0:
        try:
            propina = float(input("Propina (0 si no hay): ").replace(',', '.'))
            if propina < 0:
                print("No puede ser negativa.")
        except ValueError:
            print("Eso no es un número.")
            propina = -1

    cobrar_mesa(restaurante, numero, propina)

def mostrar_resumen_noche(restaurante):
    print("\n===== RESUMEN DE LA NOCHE =====")
    print(f"Ganancias del restaurante: {restaurante['ganancias']} €")

    total_propinas = 0
    print("Propinas por camarero:")
    for nombre in restaurante['camareros']:
        propinas = restaurante['camareros'][nombre]['propinas']
        print(f"  {nombre}: {propinas} €")
        total_propinas += propinas
    print(f"Total de propinas: {total_propinas} €")


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
            if restaurante is not None:
                guardar_menu(ruta_restaurante, restaurante)
                print("Menú guardado.")
            print("¡Hasta luego!")
            break

        elif opcion in ["2", "3", "4", "5", "6"]:
            if restaurante is None:
                print("Primero tienes que cargar un restaurante (opción 1).")
            elif opcion == "2":
                cargar_nuevos_grupos(restaurante)
            elif opcion == "6":
                mostrar_estado(restaurante)
            else:
                print("Pendiente.")

        else:
            print("Opción no válida.")

def mostrar_estado(restaurante):
    print(f"\n===== ESTADO: {restaurante['nombre']} =====")
    print(f"Ocupación: {restaurante['ocupacion']} / {restaurante['capacidad']} personas")
    print(f"Mesas: {len(restaurante['mesas'])} / {restaurante['mesas_max']}")
    print(f"Ganancias de la noche: {restaurante['ganancias']} €")

    print("\n--- Menú ---")
    for plato in restaurante['menu']:
        print(f"  {plato}: {restaurante['menu'][plato]} €")

    print("\n--- Mesas activas ---")
    if len(restaurante['mesas']) == 0:
        print("  No hay mesas ocupadas.")
    for mesa in restaurante['mesas']:
        if mesa['atendida']:
            platos = ", ".join(mesa['pedidos'])
            print(f"  Mesa {mesa['num_mesa']}: {mesa['clientes']} clientes, pedido tomado: {platos}")
        else:
            print(f"  Mesa {mesa['num_mesa']}: {mesa['clientes']} clientes, esperando pedido")

if __name__ == "__main__":
    main()