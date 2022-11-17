import modelo

def ListProp():
    base = modelo.Conectar()
    listado = base.ListarPropiedades()
    print("\n LISTADO TOTAL DE INMUEBLES ")
    print("\n|Prop|Direccion Propiedad|       Nombre      |Contacto  |Tipo Propiedad|")
    tot = 0
    for propiedad in listado:
        tot += 1
        print(" " ,propiedad[0]," " ,propiedad[1], "         " ,propiedad[2], "     " ,propiedad[3], " " ,propiedad[4])
    print("")
    input("Presione ENTER para continuar")
    print("")
    print("\n TOTAL DE INMUEBLES: ", tot)

   
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
    Localidad_Propiedad = input("\nIngresar Nombre de la Propiedad: ")
    Provincia_Propiedad = input("\nIngresar Contacto de la Propiedad: ")
    
    print()
    input("Presione ENTER para continuar ...")
    
    
    nuevaProp = modelo.propiedad(0, Id_Tipo, Id_Estado, Id_Operacion_Comercial, Id_Propietario, Direccion_Propiedad, Nombre_Propiedad, Contacto_Propiedad)
    base.InsertaProp(nuevaProp)    

    print()
    input("Presione ENTER para continuar ...")
       
def EliminarPropiedad():
    ListProp()
    Id_Propiedad = int(input("\nIngrese el Id de Propiedad a ELIMINAR: "))
    
    modelo.Conectar.EliminarPropiedad(Id_Propiedad)
    input("Presione ENTER para continuar")
    print(" ")

def ActualizarPropiedad():
    base = modelo.Conectar()
    
    print("\nListado de Propiedades:")

    for i in base.ListarPropiedades():
        print(i)    
    Id_Propiedad = int(input("\nIngrese el Id de Propiedad: "))

    Id_Tipo = 0

    Id_Estado = int(input("\nIngrese Estado - DISPONIBLE: 1 - NO DISPONIBLE: 2: "))

    Id_Operatoria_Comercial = 0
    Id_Propietario = 0    
    Direccion_Propiedad = 0
    Nombre = 0
    Contacto = 0

    print()
    input("Presione ENTER para continuar")
    

    ActualizarPropiedad = modelo.propiedad(Id_Propiedad, Id_Tipo, Id_Estado, Id_Operatoria_Comercial, Id_Propietario, Direccion_Propiedad, Nombre, Contacto)
    print(ActualizarPropiedad)
    con.ActualizarPropiedad(ActualizarPropiedad)    

    print()
    input("Presione ENTER para continuar")
    

            
