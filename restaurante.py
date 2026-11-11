## ejercicio 1
def crear_restaurante(nombre, capacidad, menu, mesas_max = -1, camareros = None):
    if camareros is None: 
        camareros = ['Pepe', 'Isaac']
    
    restaurante = {
        'nombre' : nombre,
        'capacidad' : capacidad,
        'menu' : menu,
        'mesas' : [],
        'ocupacion' : 0,
        'ganancias' : 0,
        'camareros' : {}
    }


    for camarero in camareros:
        restaurante['camareros'][camarero] = {'mesas' : 0, 'propinas' : 0} 

    if mesas_max > 0:
        restaurante['mesas_max'] = mesas_max
    return restaurante


#### PARA QUE NO TENGAMOS INFINITAS MESAS

def numero_mesa_libre(restaurante):
    ocupados = []
    for mesa in restaurante['mesas']:
        ocupados.append(mesa['num_mesa'])

    numero = 1
    while numero in ocupados:
        numero += 1
    return numero


##ejercicio 2
def insertar_mesa(restaurante, clientes):
    numero = numero_mesa_libre(restaurante)
    camarero = elegir_camarero(restaurante)
    nueva_mesa = {'num_mesa' : numero, 'clientes' : clientes, 'atendida' : False, 'camarero': camarero}
    restaurante['mesas'].insert(numero - 1, nueva_mesa)
    restaurante['ocupacion'] += clientes
    restaurante['camareros'][camarero]['mesas'] += 1
    print(f"Mesa {nueva_mesa['num_mesa']} asignada a {clientes} clientes. Camarero: {camarero}.")

def añadir_mesa(restaurante, clientes):
    if restaurante['ocupacion'] + clientes > restaurante['capacidad']:
        print('No tenemos suficiente sitio')
        return

    if 'mesas_max' in restaurante:
        if len(restaurante['mesas']) < restaurante['mesas_max']:
            insertar_mesa(restaurante, clientes)
        else:
            print('No caben mas grupos')
            return
    else:
        insertar_mesa(restaurante, clientes)


#### SENTAMOS A LOS GRUPOS

def sentar_grupos(restaurante, grupos):
    for grupo in grupos:
        añadir_mesa(restaurante, grupo['clientes'])


#### MESAS PEDIENTES 

def mesas_pendientes(restaurante):
    pendientes = []
    for mesa in restaurante['mesas']:
        if mesa['atendida'] == False:
            pendientes.append(mesa)
    return pendientes


#### MESAS ATENTIDAS

def mesas_atendidas(restaurante):
    atendidas = []
    for mesa in restaurante['mesas']:
        if mesa['atendida'] == True:
            atendidas.append(mesa)
    return atendidas



## ejercicio 3
def tomar_pedido(mesa, menu):
    pedidos = []
    for cliente in range(mesa['clientes']):
        pedido = input('¿Que quiere tomar?: ')
        num_platos = 0
        while (pedido != 'Eso es todo' or num_platos == 0):
            if pedido in menu:
                pedidos.append(pedido)
                num_platos += 1
            elif pedido == 'Eso es todo':
                print('Tiene que pedir al menos un plato')
            else:
                print(f'No tenemos {pedido}')
            pedido = input('¿Quiere tomar algo mas?: ')
    mesa['pedidos'] = pedidos
    mesa['atendida'] = True



## ejercicio 4
def calcular_cuenta(mesa, menu):
    total = 0
    for pedido in mesa['pedidos']:
        precio = menu[pedido]
        total += precio
    mesa['cuenta'] = total
    return total


## ejercicio 5
def atender_todas_las_mesas(restaurante):
    for mesa in restaurante['mesas']:
        if mesa['atendida'] == False:
            tomar_pedido(mesa, restaurante['menu'])
            calcular_cuenta(mesa, restaurante['menu'])


#### COBRAR Y LIBERAR LAS MESAS

def buscar_mesa(restaurante, num_mesa):
    for mesa in restaurante['mesas']:
        if mesa['num_mesa'] == num_mesa:
            return mesa
    return None



def cobrar_mesa(restaurante, num_mesa, propina = 0):
    mesa = buscar_mesa(restaurante, num_mesa)

    if mesa is None:
        print(f'No existe la mesa {num_mesa}')
        return None

    if mesa['atendida'] == False:
        print(f'La mesa {num_mesa} todavía no ha pedido, no se puede cobrar')
        return None


    total = calcular_cuenta(mesa, restaurante['menu'])
    restaurante['ganancias'] += total
    restaurante['ocupacion'] -= mesa['clientes']
    
    camarero = mesa['camarero']
    restaurante['camareros'][camarero]['propinas'] += propina
    restaurante['camareros'][camarero]['mesas'] -= 1
    
    restaurante['mesas'].remove(mesa)

    print(f'Mesa {num_mesa} cobrada: {total} €. Ganancias de la noche: {restaurante["ganancias"]} €')
    return total


#### PARA AMPLIAR EL MENÚ

def ampliar_menu(restaurante):
    nombre = input('Nombre del nuevo plato: ').strip()

    if nombre == '':
        print('El nombre no puede estar vacío')
        return False

    if nombre == 'Eso es todo':
        print('"Eso es todo" no puede ser un plato: es la frase para terminar un pedido')
        return False

    if nombre in restaurante['menu']:
        print(f'"{nombre}" ya está en el menú a {restaurante["menu"][nombre]} €. Se actualizará su precio.')

    precio = 0
    while precio == 0:
        try:
            numero = float(input('Precio del nuevo plato: ').replace(',', '.'))
            if numero > 0:
                precio = numero
            else:
                print('El precio tiene que ser mayor que 0')
        except ValueError:
            print('Eso no es un número válido. Ejemplo: 8 o 8.5')

    restaurante['menu'][nombre] = precio
    print(f'Menú actualizado: {nombre} -> {precio} €')
    return True


#### FEATURES CALLE 365

# Vamos a delegar tareas según QUÉ tan ocupado esté cada camarero

def elegir_camarero(restaurante):
    elegido = None
    for nombre in restaurante['camareros']:
        if elegido is None or restaurante['camareros'][nombre]['mesas'] < restaurante['camareros'][elegido]['mesas']:
            elegido = nombre
    return elegido




if __name__ == "__main__":
    restaurante = crear_restaurante("Casa Pepe", 50, {'Sopa' : 3, 'Macarrones' : 6, 'Ensalada' : 4}, 2)



    print(f"\n\nSentar grupos. Nuevo")
    grupos = [{"clientes": 4}, {"clientes": 3}, {"clientes": 2}]
    sentar_grupos(restaurante, grupos)
    print(restaurante)




    print("\n\nMesas pendientes y atendidas. Nuevo")
    restaurante['mesas'][0]['pedidos'] = ['Sopa', 'Macarrones']
    restaurante['mesas'][0]['atendida'] = True
    print("Pendientes:", mesas_pendientes(restaurante))
    print("Atendidas:", mesas_atendidas(restaurante))




    # añadir_mesa(restaurante, 3)
    # añadir_mesa(restaurante, 4)
    # print(restaurante)



    # tomar_pedido(restaurante['mesas'][0], restaurante['menu'])
    # print(restaurante['mesas'][0])



    # calcular_cuenta(restaurante['mesas'][0], restaurante['menu'])
    # print(restaurante['mesas'][0])



    # atender_todas_las_mesas(restaurante)
    # print(restaurante)



    # for mesa in restaurante['mesas']:
    #     print(mesa)



    print("\n\nCobrar mesa. Nuevo")
    cobrar_mesa(restaurante, 7)     # no existe
    cobrar_mesa(restaurante, 2)     # no ha pedido
    cobrar_mesa(restaurante, 1,2)     # todo nice. Deberíamos poder
    print(restaurante)
    print("Camareros:", restaurante['camareros'])

    print("\n\nLlega un grupo nuevo después de liberar la mesa 1")
    añadir_mesa(restaurante, 5)
    print(restaurante['mesas'])

    print('\n\nAmpliar menú. Nuevo')
    ampliar_menu(restaurante)
    ampliar_menu(restaurante)
    print(restaurante['menu'])

