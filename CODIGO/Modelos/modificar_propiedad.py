Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def modifica_propiedad():
    try:
        conecta()
        print("modifica propiedad para administrar")
        print()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return

def borra_propiedad():
    try:
        conecta()
        print("borra propiedad para administrar")
        print("No tiene funcionalidad todavia")        
        print()
        time.sleep(3)
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        conecta_mal()
    return