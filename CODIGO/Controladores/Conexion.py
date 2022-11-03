import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
        host = 'localhost',
        port= 3306,
        user = 'root',
        password= '',
        db= 'db_inmobiliaria'
    )

        if conexion.is_connected():
            print("LA CONEXIÓN FUE EXITOSA")

        cursor = conexion.cursor(buffered=True)
        return [conexion,cursor]

    except:
        print("NO SE PUDO CONECTAR A LA BASE DE DATOS")
