from conexionSQL import *

class cusuarios:
    def mostrarTurnos():
        try:
            cone = cconexion.conexionYuyito()
            cursor = cone.cursor()
            sql = "select * from usuario order by turno"
            cursor.execute(sql)
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
        except oracledb.Error as error:
            print ("Error de extraer datos", error)
            return

    def ingresarDatosU(rut, nombre, telefono):
        try:
            cone = cconexion.conexionYuyito()
            cursor = cone.cursor()
            sql = "insert into usuario values (:1,:2, :3)"
            valores = (rut, nombre, telefono)
            cursor.execute(sql,valores)
            cone.commit()
            print (cursor.rowcount, "Turno obtenido")
            cone.close()
            numTurn
        except oracledb.Error as error:
            print ("Error de ingreso de datos", error)

    def consultarTurno():
        

    def cancelarTurno(usuario):
        try:
            cone = cconexion.conexionYuyito()
            cursor = cone.cursor()
            sql = "delete from usuarios where usuarios.usuario = :1"
            valores = (usuario,)
            cursor.execute(sql,valores)
            cone.commit()
            print (cursor.rowcount, "Registro Eliminado")
            cone.close
        except oracledb.Error as error:
            print ("Error de Eliminación de datos")
        