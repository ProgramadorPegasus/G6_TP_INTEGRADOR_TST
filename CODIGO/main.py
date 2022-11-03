from itertools import combinations_with_replacement
import time
from os import system
import Controladores.Conexion as inmobiliaria

def ver_conexion():          
    try:
        print("Por favor espere, verificando Conexión base de datos")
        inmobiliaria.conectar()
        time.sleep(2)
        
    except:
        print("Error de conexion, no se pude establecer vinculo a base de datos: ")
        
    return

salir = False

# Issue #2 Hacer codigo para Ingresar propiedad  - PEDRO ROJO
def ingresar_Propiedad():
    ver_conexion()
    datos=("INSERT INTO db_inmobiliaria.propiedad (Id_Propiedad, Id_Tipo, Id_Estado, Id_Operatoria_Comercial) VALUES ("10","2","1","1","10","Juan Perez","Carlos Paz","43253443"))
    # datos = ("INSERT INTO db_inmobiliaria.propiedad (Id_Propiedad, Id_Tipo, Id_Estado, Id_Operatoria_Comercial) VALUES (%s, %s, %s, %s)")
    inmobiliaria.execute(datos)
    inmobiliaria.commit()

# Issue #5 Reporte - Listado de propiedades TOTALES, sin distincion de estado  - PEDRO ROJO
def listarPropiedades(self):
    cursor=inmobiliaria.cursor()
    cursor.execute("SELECT Nombre_Estado, Nombre_Tipo, P.Nombre, P.Direccion, P.Contacto, Pr.Nombre, Pr.Direccion, Pr.Contacto FROM  Propiedad Pr inner join Estado E on  Pr.Id_Estado=E.Id_Estado inner join Propietario P on Pr.Id_Propietario=P.Id_Propietario inner join Tipo T on Pr.Id_Tipo=T.Id_Tipo;")
    for x in cursor:
        print(x)
    inmobiliaria.close()
    print("CONEXION CERRADA EXITOSAMENTE")



menu=("""\
-----------------------------------------------------------------------
|         Inmobiliaria Bienes Raices Future                           |
-----------------------------------------------------------------------
|                                                                     |
| 1. Probar conexion Base de Datos                                           |
| 2. Ingresar Nueva propiedad                                         |
| 3. Modificar propiedad                                              |
| 4. Eliminar  propiedad                                              |
| 5. Listar todas las propiedades                                     |
| 6. Listar propiedades disponibles para la venta                     |
| 7. Listar propiedades disponibles para alquiler                     |
| 8. Listar propiedades vendidas                                      |
| 9. Listar propiedades alquiladas                                    |
|                                                                     |
| 0. Salir                                                            |
|                                                                     |
-----------------------------------------------------------------------\
 """)

while not salir:
    print(menu)
    try:
        opcion = int(input("Por favor, ingrese una opción: "))
        print()
               
        if opcion == 1:
            ver_conexion()
        elif opcion == 2:  # Issue #2 Hacer codigo para Ingresar propiedad  - PEDRO ROJO
            print('Ingresar Nueva Propiedad:')
            time.sleep(2)
            ingresar_Propiedad()
        elif opcion == 5: # Issue #5 Reporte - Listado de propiedades TOTALES, sin distincion de estado  - PEDRO ROJO
            print('Listar todas las propiedades:')
            time.sleep(2)
            listarPropiedades()
        elif opcion == 0:
            print('Hasta luego ... !!!')
            salir = True
            time.sleep(1)
            system("cls")
            break
    except:
        print()
        print('OPCIÓN INCORRECTA')
        print()
        continua = input('PRESIONE CUALQUIER TECLA')
        system("cls")
