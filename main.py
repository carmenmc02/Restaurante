def mostrar_menu():
    print("\n===== GESTOR DEL RESTAURANTE =====")
    print("1. Cargar restaurante")
    print("2. Cargar nuevos grupos")
    print("3. Tomar un pedido")
    print("4. Cobrar y liberar una mesa")
    print("5. Ampliar el menú")
    print("6. Consultar estado")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "7":
            print("¡Hasta luego!")
            break
        elif opcion in ["1", "2", "3", "4", "5", "6"]:
            print("Pendiente.")
        else:
            print("Opción no válida.")