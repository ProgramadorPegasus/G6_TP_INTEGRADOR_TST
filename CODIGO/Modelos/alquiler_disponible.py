
#-- Listado de propiedades DISPONIBLES para alquiler --#
    def ListarPropiedadesDisponiblesAlquiler(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr inner join db_inm_brf.`Estado` as es on  pr.Id_Estado = es.Id_Estado inner join db_inm_brf.`operatoria comercial` as op on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial where op.Id_Operatoria_Comercial = 2 and es.Id_Estado = 1 order by pr.Id_Propiedad;")
                resultados = cursor.fetchall()
                self.conexion.close()
                print("MySQL connection is closed")
                return resultados
            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)
