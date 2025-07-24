import oracledb

class cconexion:
    def conexionYuyito():
        try:
            conexion=oracledb.connect(
            user='YUYITO',
            password='1234',
            dsn='localhost:1521/xepdb1')
            return conexion
        
        except oracledb.Error as e:
            print ("Error al conectar a la base de datos {}".format(e))    
            return conexion

    conexionYuyito()