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
if __name__ == "__main__":
    codigo = True
    while codigo == True:
        print("1. Registrar \
        2. Listar \
        3. Salir del sistema ")
        operacion = int(input())

        while (operacion == 1):
            print("1. Pieza \
            2. Máquina \
            3. Cliente \
            4. Pedido \
            5. Reposición \
            6. Salir ")
            regis = int(input())
                #Metemos todas las opciones
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

            if lis == 6:
                break
        
        if operacion == 3:
            break