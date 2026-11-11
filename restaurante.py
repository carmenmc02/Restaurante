
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


def numero_mesa_libre(restaurante):
    ocupados = []
    for mesa in restaurante['mesas']:
        ocupados.append(mesa['num_mesa'])

    numero = 1
    while numero in ocupados:
        numero += 1
    return numero

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


#### MESAS PENDIENTES 

def mesas_pendientes(restaurante):
    pendientes = []
    for mesa in restaurante['mesas']:
        if mesa['atendida'] == False:
            pendientes.append(mesa)
    return pendientes


#### MESAS ATENDIDAS

def mesas_atendidas(restaurante):
    atendidas = []
    for mesa in restaurante['mesas']:
        if mesa['atendida'] == True:
            atendidas.append(mesa)
    return atendidas

def tomar_pedido(mesa, menu):
    pedidos = []
    while len(pedidos) == 0:
        for cliente in range(mesa['clientes']):
            print(f"Cliente {cliente + 1}:")
            pedido = input('¿Qué quiere tomar?: ')
            while pedido != 'Eso es todo':
                if pedido in menu:
                    pedidos.append(pedido)
                else:
                    print(f'No tenemos {pedido}')
                pedido = input('¿Quiere tomar algo más?: ')
        if len(pedidos) == 0:
            print('Al menos uno de ustedes tiene que pedir un plato.')
            respuesta = input('¿Quieren intentarlo otra vez? (s/n): ').strip().lower()
            while respuesta != 's' and respuesta != 'n':
                respuesta = input('Responde s o n: ').strip().lower()
            if respuesta == 'n':
                return False
    mesa['pedidos'] = pedidos
    mesa['atendida'] = True
    return True

def liberar_mesa(restaurante, mesa):
    restaurante['ocupacion'] -= mesa['clientes']
    restaurante['camareros'][mesa['camarero']]['mesas'] -= 1
    restaurante['mesas'].remove(mesa)

def calcular_cuenta(mesa, menu):
    total = 0
    for pedido in mesa['pedidos']:
        precio = menu[pedido]
        total += precio
    mesa['cuenta'] = total
    return total

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