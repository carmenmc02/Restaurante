## ejercicio 1
def crear_restaurante(nombre, capacidad, menu, mesas_max = -1):
    restaurante = {
        'nombre' : nombre,
        'capacidad' : capacidad,
        'menu' : menu,
        'mesas' : [],
        'ocupacion' : 0,
        'ganancias' : 0,
        'siguiente_mesa' : 1
    }

    if mesas_max > 0:
        restaurante['max_mesas'] = mesas_max
    return restaurante



##ejercicio 2
def insertar_mesa(restaurante, clientes):
    nueva_mesa = {'num_mesa' : restaurante['siguiente_mesa'] + 1, 'clientes' : clientes, 'atendida' : False}
    restaurante['mesas'].append(nueva_mesa)
    restaurante['ocupacion'] += clientes
    restaurante['siguiente_mesa'] += 1
    print(f"Mesa {nueva_mesa['num_mesa']} asignada a {clientes} clientes.")

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






if __name__ == "__main__":
    restaurante = crear_restaurante("Casa Pepe", 50, {'Sopa' : 3, 'Macarrones' : 6, 'Ensalada' : 4}, 2)

    añadir_mesa(restaurante, 3)
    añadir_mesa(restaurante, 4)
    print(restaurante)

    tomar_pedido(restaurante['mesas'][0], restaurante['menu'])
    print(restaurante['mesas'][0])

    calcular_cuenta(restaurante['mesas'][0], restaurante['menu'])
    print(restaurante['mesas'][0])

    atender_todas_las_mesas(restaurante)
    print(restaurante)

    for mesa in restaurante['mesas']:
        print(mesa)

