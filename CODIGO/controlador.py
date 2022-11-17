import modelo

def ListProp():
    con = modelo.Conectar()
    listado = con.ListarPropiedades()
    print("\n LISTADO TOTAL DE INMUEBLES ")
    print("\n|Prop|Direccion Propiedad|       Localidad      |Provincia|Tipo Propiedad|")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" " ,propiedad[0]," " ,propiedad[1], "         " ,propiedad[2], "     " ,propiedad[3], " " ,propiedad[4])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES: ", tot)

###########################################################################################
    
def ListarPropiedadesDisponiblesVenta():
    con = modelo.Conectar()
    listado = con.ListarPropiedadesDisponiblesVenta()
    print("\n LISTADO INMUEBLES DISPONIBLES PARA VENTA ")
    print("\n|Prop|Direccion Propiedad       | Estado   | Operatoria Comercial |")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" ",propiedad[0]," " ,propiedad[1], "       " ,propiedad[2], "   " ,propiedad[3])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES PARA VENTA: ", tot)

###########################################################################################
    
def ListarPropiedadesDisponiblesAlquiler():
    con = modelo.Conectar()
    listado = con.ListarPropiedadesDisponiblesAlquiler()
    print("\n LISTADO INMUEBLES DISPONIBLES PARA ALQUILAR ")
    print("\n|Prop|Direccion Propiedad| Estado   | Operatoria Comercial |")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" ",propiedad[0]," " ,propiedad[1], "       " ,propiedad[2], "   " ,propiedad[3])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES PARA ALQUILAR: ", tot)

###########################################################################################

def ListarPropiedadesVendidas():
    con = modelo.Conectar()
    listado = con.ListarPropiedadesVendidas()
    print("\n LISTADO INMUEBLES VENDIDOS ")
    print("\n|Prop|Direccion Propiedad| Estado   | Operatoria Comercial |")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" ",propiedad[0]," " ,propiedad[1], "       " ,propiedad[2], "   " ,propiedad[3])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES VENDIDOS: ", tot)

###########################################################################################

def ListarPropiedadesAlquiladas():
    con = modelo.Conectar()
    listado = con.ListarPropiedadesAlquiladas()
    print("\n LISTADO INMUEBLES ALQUILADOS ")
    print("\n|Prop|Direccion Propiedad       | Estado   | Operatoria Comercial |")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" ",propiedad[0]," " ,propiedad[1], "       " ,propiedad[2], "   " ,propiedad[3])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES ALQUILADOS: ", tot)

###########################################################################################
            
def ListarTipoPropiedad():
    con = modelo.Conectar()
    listado = con.ListarTipoPropiedad
    print("\n LISTADO TIPOS DE PROPIEDADES ")
    print("\n| Tipo Propiedad |Descripcion Tipo       |")
    for propiedad in listado:
        print(" " ,propiedad[0],"   " ,propiedad[1])
    print("")
    input("Presione ENTER para continuar")

def ListarPropietarios():
    con = modelo.Conectar()
    listado = con.ListarPropietarios
    print("\n LISTADO DE PROPIETARIOS ")
    print("\n| Id Propietario | Nombre de Popietario       |")
    for propiedad in listado:
        print(" " ,propiedad[0],"   " ,propiedad[1])
    print("")
    input("Presione ENTER para continuar")

###########################################################################################        
    
def InsertaProp():
    base = modelo.Conectar()
    
    print("\nTipo de Propiedades:")
    for i in base.ListarTipoPropiedad():
        print(i)    
    Id_Tipo = int(input("\nIngresar el Tipo de Propiedad: "))

    Id_Estado = int(input("\nIngresar Estado - DISPONIBLE: 1 - NO DISPONIBLE: 2: "))
    Id_Operacion_Comercial = int(input("\nIngrese el Tipo de Operatoria Comercial - VENTA: 1 - ALQUILER: 2: "))
    Id_Propietario = int(input("\nIngrese el Id. de Propietario: "))
    Direccion_Propiedad = input("\nIngresar Direccion de la Propiedad: ")
    Localidad_Propiedad = input("\nIngresar Localidad de la Propiedad: ")
    Provincia_Propiedad = input("\nIngresar Provincia de la Propiedad: ")
    
    print()
    input("Presione ENTER para continuar ...")
    print()

    
    nuevaProp = modelo.propiedad(0, Id_Tipo, Id_Estado, Id_Operacion_Comercial, Id_Propietario, Direccion_Propiedad, Localidad_Propiedad, Provincia_Propiedad)
#    print(nuevaPropiedad)
    base.InsertaProp(nuevaProp)    

    print()
    input("Presione ENTER para continuar ...")
    print()

###########################################################################################
       
def EliminarPropiedad():
    ListProp()
    Id_Propiedad = int(input("\nIngrese el Id de Propiedad a ELIMINAR: "))
    
    modelo.Conectar.EliminarPropiedad(Id_Propiedad)
    input("Presione ENTER para continuar")
    print(" ")

###########################################################################################

def ActualizarPropiedad():
    con = modelo.Conectar()
    
    print("\nListado de Propiedades:")

    for i in con.ListarPropiedades():
        print(i)    
    Id_Propiedad = int(input("\nIngrese el Id de Propiedad: "))

    Id_Tipo = 0

    Id_Estado = int(input("\nIngrese Estado - DISPONIBLE: 1 - NO DISPONIBLE: 2: "))

    Id_Operacion_Comercial = 0
    Id_Propietario = 0    
    Direccion_Propiedad = 0
    Localidad = 0
    Provincia = 0

    print()
    input("Presione ENTER para continuar")
    print()

    ActualizarPropiedad = modelo.propiedad(Id_Propiedad, Id_Tipo, Id_Estado, Id_Operacion_Comercial, Id_Propietario, Direccion_Propiedad, Localidad, Provincia)
    print(ActualizarPropiedad)
    con.ActualizarPropiedad(ActualizarPropiedad)    

    print()
    input("Presione ENTER para continuar")
    print()

            