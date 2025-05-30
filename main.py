# 1. Registrar
#     1. Pieza
#     2. Máquina
#     3. Cliente
#     4. Pedido
#     5. Reposición
#     6. Salir
# 2. Listar
#     1. Clientes
#     2. Pedidos
#     3. Máquinas
#     4. Piezas
#     5. Contabilidad
#     6. Salir
# 3. Salir del Sistema
from entities.sistema import Sistema
sistema = Sistema()
if __name__ == "__main__":
    codigo = True
    while codigo == True:
        print("1. Registrar \
        2. Listar \
        3. Salir del sistema ")
        operacion = int(input())

        while operacion == 1:
            print("1. Pieza \
            2. Máquina \
            3. Cliente \
            4. Pedido \
            5. Reposición \
            6. Salir ")
            regis = int(input())
            if regis == 1:
                descripcion = input("Ingrese la descripción de la pieza: ")
                costo = float(input("Ingrese el costo de la pieza: "))
                tamaño_lote = int(input("Ingrese el tamaño del lote: "))
                sistema.registrar_pieza(descripcion, costo, tamaño_lote, cantidad_disponible)
            if regis == 3:
                print("1. Empresa \
                2. Particular \
                ")
                rcli = int(input())
                if rcli == 1:
                    sistema.registrar_empresa(int(input("Ingrese el télefono ")),input("Ingrese el correo "), int(input("Ingrese el RUT ")), input("Ingrese el nombre "), input ("Ingrese la página web "))
                else:
                    sistema.registrar_particular (int(input("Ingrese el télefono ")), input("Ingrese el correo "), int(input("Ingrese la cédula " )), input ("Ingrese su nombre completo ")   )            
            if regis == 4:
                clientes = Sistema.select_cliente()
                maquina = Sistema.select_maquina()
                estado, fecha_entregado = Sistema.entrega(stock)
                Sistema.registrar_pedido(clientes, maquina, fecha_entregado, estado)
            if regis == 5:
                sistema.reponer()
            if regis == 6:
                break
                



        while operacion == 2:
            print("1. Clientes \
            2. Pedidos \
            3. Máquinas \
            4. Piezas\
            5. Contabilidad\
            6. Salir ")
            lis = int(input())

            if lis == 1:
                sistema.listar_emp()
                sistema.listar_par()
            
            if lis == 4:
                sistema.listar_piezas()

            if lis == 6:
                break
        
        if operacion == 3:
            break
