import controlador

while True:
    print("===============================================")
    print("|    TRABAJO PRACTICO INTEGRADOR GRUPO 6      | ")
    print("|                INMOBILIARIA                 |") 
    print("|            BIENES RAICES FUTURE             |")
    print("===============================================")
    print("")
    print("============== MENÚ PRINCIPAL =================")
    print("|  1 - INGRESAR PROPIEDAD                     |")
    print("|  2 - MODIFICAR PROPIEDAD                    |")
    print("|  3 - ELIMINAR PROPIEDAD                     |")
    print("|  4 - LISTADO DE PROPIEDADES                 |")
    print("|  5 - PROPIEDADES DISPONIBLES PARA VENTA     |")
    print("|  6 - PROPIEDADES DISPONIBLES PARA ALQUILER  |")
    print("|  7 - PROPIEDADES VENDIDAS                   |")
    print("|  8 - PROPIEDADES ALQUILADAS                 |")
    print("|  9 - SALIR                                  |")
    print("===============================================")

    print("")
    opc = int(input("Seleccione una opción: "))
    
    if opc == 1:
       controlador.InsertaProp()   # Issue 2 - Pedro Rojo
   
    elif opc == 4:  
        controlador.ListProp() #  Issue 5 - Pedro Rojo

    elif opc == 9:
        print("")
        print("===============================================")
        print("===== ¡SALIENDO DEL SISTEMA - HASTA LUEGO ! ===")
        print("===============================================")
        print("")
        break

    else:
            print("Opcion incorrecta, por favor seleccionar entre 1 y 9.")
            print("")
            