## ejercicio 1
def crear_restaurante(nombre, aforo, menu, max_mesas = -1):
    restaurante = {
        'nombre' : nombre,
        'aforo' : aforo,
        'menu' : menu,
        'mesas' : [],
        'ocupacion' : 0
    }

    if max_mesas > 0:
        restaurante['max_mesas'] = max_mesas
    return restaurante



##ejercicio 2
def insertar_mesa(restaurante, clientes):
    nueva_mesa = {'num_mesa' : len(restaurante['mesas']) + 1, 'clientes' : clientes, 'atendida' : False}
    restaurante['mesas'].append(nueva_mesa)
    restaurante['ocupacion'] += clientes


def añadir_mesa(restaurante, clientes):
    if restaurante['ocupacion'] + clientes > restaurante['aforo']:
        print('No tenemos suficiente sitio')
        return

    if 'max_mesas' in restaurante:
        if len(restaurante['mesas']) < restaurante['max_mesas']:
            insertar_mesa(restaurante, clientes)
        else:
            print('No caben mas grupos')
            return
    else:
        insertar_mesa(restaurante, clientes)




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




