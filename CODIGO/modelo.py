import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'db_inmobiliaria'

            )
        except mysql.connector.Error as  desErr:
            print("¡ NO SE PUDO CONECTAR A LA BASE DE DATOS",desErr)

#-- Issue 4 Listado de propiedades TOTALES, sin distinción de estados --  Pedro Rojo
            
    def ListProp(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select propiedad.Id_Propiedad, propiedad.Direccion_Propiedad, propiedad.Nombre, propiedad.Contacto, tipo.Nombre_Tipo from db_inmobiliaria.`Propiedad` inner join db_inmobiliaria.`tipo` on  propiedad.Id_Tipo = tipo.Id_Tipo order by propiedad.Id_Propiedad")
                res = cursor.fetchall()
                self.conexion.close()
                return res
            
            except mysql.connector.Error as  desErr:
                print("¡ NO SE PUDO CONECTAR A LA BASE DE DATOS",desErr)
                
#-- Issue 2 Insertar una propiedad --  Pedro Rojo  
    def InsertaProp(self,propiedad):
        base = Conectar()
        if base.conexion.is_connected():
            try:
                cursor = base.conexion.cursor()
                ordenSQL = "INSERT INTO db_inmobiliaria.propiedad (Id_Propiedad, Id_Tipo, Id_Estado, Id_Operatoria_Comercial, Id_Propietario, Nombre, Direccion, Contacto) VALUES (null,%s,%s,%s,%s,%s,%s,%s)"

                data = (propiedad.getId_Tipo(),                    
                propiedad.getId_Estado(),
                propiedad.getId_Operatoria_Comercial(),
                propiedad.getId_Propietario(),
                propiedad.getDireccion_Propiedad(),
                propiedad.getNombre(),
                propiedad.getContacto())   
                cursor.execute(ordenSQL,data)
                base.conexion.commit()
                base.conexion.close()
                print()
                print("===== ¡PROPIEDAD INSERTADA! =====")
                print()

            except mysql.connector.Error  as descripcionError:
                print("¡NO SE CONECTO A LA BASE DE DATOS!",descripcionError)

                              
    def EliminarPropiedad(Id_Propiedad):
        base = Conectar()
        if base.conexion.is_connected():
            try:
                cursor = base.conexion.cursor()
                sentenciaSQL = "DELETE FROM db_inmobiliaria.propiedad WHERE Id_Propiedad = %s"

                cursor.execute(sentenciaSQL, (Id_Propiedad,))

                base.conexion.commit()
                base.conexion.close()
                print("PROPIEDAD ELIMINADA ...")               
            except mysql.connector.Error  as descripcionError:
                print("¡NO SE CONECTO A LA BASE DE DATOS!",descripcionError)
                
               
class propiedad():
    def __init__(self,Id_Propiedad,Id_Tipo,Id_Estado,Id_Operatoria_Comercial,Id_Propietario,Direccion_Propiedad,Nombre,Contacto) -> None:
        self.Id_Propiedad = Id_Propiedad
        self.Id_Tipo = Id_Tipo
        self.Id_Estado = Id_Estado
        self.Id_Operatoria_Comercial = Id_Operatoria_Comercial
        self.Id_Propietario = Id_Propietario
        self.Direccion_Propiedad = Direccion_Propiedad        
        self.Nombre = Nombre
        self.Contacto = Contacto

    def getId_Propiedad(self):
        return self.Id_Propiedad
    def getId_Tipo(self):
        return self.Id_Tipo
    def getId_Estado(self):
        return self.Id_Estado
    def getId_Operatoria_Comercial(self):
        return self.Id_Operatoria_Comercial
    def getId_Propietario(self):
        return self.Id_Propietario
    def getDireccion_Propiedad(self):
        return self.Direccion_Propiedad
    def getNombre(self):
        return self.Nombre
    def getContacto(self):
        return self.Contacto

    def setId_Propiedad(self,Id_Propiedad):
        self.Id_Propiedad = Id_Propiedad
    def setId_Tipo(self, Id_Tipo):
        self.Id_Tipo = Id_Tipo
    def setId_Estado(self, Id_Estado):
        self.Id_Estado = Id_Estado
    def setId_Operatoria_Comercial(self, Id_Operatoria_Comercial):
        self.Id_Operatoria_Comercial = Id_Operatoria_Comercial
    def setId_Propietario(self, Id_Propietario):
        self.Id_Propietario = Id_Propietario
    def setDireccion_Propiedad(self, Direccion_Propiedad):
        self.Direccion_Propiedad = Direccion_Propiedad
    def setNombre(self, Nombre):
        self.Nombre = Nombre
    def setContacto(self, Contacto):
        self.Contacto = Contacto

    def __str__(self) -> str:
        return str(self.Id_Propiedad) + ' ' + str(self.Id_Tipo) +' ' + str(self.Id_Estado) +' ' + str(self.Id_Operatoria_Comercial) +' ' + str(self.Id_Propietario) +' ' + str(self.Direccion_Propiedad) +' ' + str(self.Nombre) +' ' + str(self.Contacto)

   
