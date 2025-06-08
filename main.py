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
                sistema.registrar_pieza(descripcion, costo, tamaño_lote)
            
            if regis == 2:
                descripcion = input("Ingrese la descripción de la maquina: ")
                if len(sistema.piezas) == 0:
                    print("No hay piezas registradas en el sistema")
                else:
                    codigos_piezas = []
                    cantidades = []
                    
                    seguir = "si"
                    while seguir.lower() == "si":
                        print("Piezas disponibles: ")
                        for i in range(len(sistema.piezas)):
                            pieza = sistema.piezas[i]
                            print(f"Código: {pieza.codigo} - {pieza.descripcion}")
                    
                        codigo = int(input("Ingrese el código de la pieza a agregar: "))
                        cantidad = int(input("Cantidad necesaria de esa pieza: "))
                    
                        codigos_piezas.append(codigo)
                        cantidades.append(cantidad)

                        seguir =input("¿Desea agregar otra pieza? (si/no): ")
                    
                    sistema.registrar_maquina(descripcion, codigos_piezas,cantidades)
            
            if regis == 3:
                print("1. Empresa \
            2. Particular \
            ")
                rcli = int(input())
                if rcli == 1:
                        cliente_existe=True
                        while cliente_existe==True:
                            try: 
                                nomE=input("Ingrese el nombre ")
                                sistema.validar_empresa(nomE)
                                cliente_existe=False
                            except:
                                print ("El cliente ya está registrado")
                        rut_invalido=True
                        while rut_invalido:
                            while True:
                                try:
                                    rut = int(input("Ingrese la RUT " ))
                                    break
                                except:
                                    print("EL RUT debe ser un número ")
                            try: 
                                sistema.validar_rut(rut)
                                rut_invalido = False
                            except:
                                print ("EL RUT es inválida, vuelve a ingresarla")
                        telefono_invalido=True
                        while telefono_invalido:
                            while True:
                                try:
                                    tel= int(input("Ingrese el télefono "))
                                    break
                                except:
                                    print("El telefóno debe ser un número")
                            try:
                                sistema.validar_telefono(tel)
                                telefono_invalido=False
                            except: 
                                print("El télefono es inválido, vuelva a ingresarlo ")
                        correo_invalido=True
                        while correo_invalido==True:
                            try: 
                                correo=input("Ingrese el correo ")
                                sistema.validar_correo(correo)
                                correo_invalido=False
                            except:
                                print ("El correo es inválido")
                        pagina_invalida=True
                        while pagina_invalida==True:
                            try: 
                                pagina=input("Ingrese la página web ")
                                sistema.validar_pagina(pagina)
                                pagina_invalida=False
                            except:
                                print ("La página es inválida")
                        sistema.registrar_empresa(tel,correo, rut , nomE , pagina) 
                        print("El cliente ha sido registrado")

                else:
                        while cliente_existe==True:
                            try: 
                                nomP=input("Ingrese el nombre ")
                                sistema.validar_particular(nomP)
                                cliente_existe=False
                            except:
                                print ("El cliente ya está registrado")

                        cedula_invalida=True
                        while cedula_invalida:
                            while True:
                                try:
                                    ci = int(input("Ingrese la cédula " ))
                                    break
                                except:
                                    print("La cédula debe ser un número ")
                            try: 
                                sistema.validar_cedula(ci)
                                cedula_invalida = False
                            except:
                                print ("La cédula es inválida, vuelve a ingresarla")
                        
                        telefono_invalido=True
                        while telefono_invalido:
                            while True:
                                try:
                                    tel= int(input("Ingrese el télefono "))
                                    break
                                except:
                                    print("El telefóno debe ser un número")
                            try:
                                sistema.validar_telefono(tel)
                                telefono_invalido=False
                            except: 
                                print("El télefono es inválido, vuelva a ingresarlo ")
                        
                        correo_invalido=True
                        while correo_invalido==True:
                            try: 
                                correop=input("Ingrese el correo ")
                                sistema.validar_correo(correop)
                                correo_invalido=False
                            except:
                                print ("El correo es inválido")
                        cliente_existe=True
                        
                        sistema.registrar_particular (tel,correop, ci, nomP)    
                        print ("El cliente ha sido registrado con éxito")
                
            if regis == 4:
                clientes = Sistema.select_cliente(sistema)
                if clientes == False:
                    print ("No se puede continuar. Aun no hay Clientes registrados")
                    break
                maquina = Sistema.select_maquina(sistema)
                if maquina == False:
                    print ("No se puede continuar. Aun no hay Maquinas registradas")
                    break
                estado, lista_piezas_faltantes = Sistema.entrega(sistema, maquina)
                fecha_entregado = Sistema.fecha_entrega(estado)
                precio = Sistema.pre(clientes, maquina)
                Sistema.registrar_pedido(sistema, clientes, maquina, fecha_entregado, estado, precio, lista_piezas_faltantes)
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
            
            if lis == 2:
                sistema.listar_pedidos()

            if lis == 3:
                sistema.listar_maquinas()
            
            if lis == 4:
                sistema.listar_piezas()

            if lis == 5:
                sistema.contabilidad()

            if lis == 6:
                break
        
        if operacion == 3:
            break
