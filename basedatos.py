import sqlite3 as sql
import pandas as pd
from tabulate import tabulate

class Basededatos():
    
#FUNCION PARA CREAR UNA BASE DE DATOS
    def createDB(BaseDatos):
        conn = sql.connect(BaseDatos)
        conn.commit()
        conn.close()
        return BaseDatos

#FUNCION PARA CREAR UNA TABLA EN LA BASE DE DATOS
    def create_Table(
        BaseDatos,table):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table}
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0,
                    Producto TEXT UNIQUE,
                    Precio REAL) """)       
        conn.commit()
        conn.close()
        return table

#FUNCION PARA INSERTAR UN NUEVO PRODUCTO Y SU PRECIO EN LA BASE DE DATOS
    def insertRow(BaseDatos,table, producto, precio):
        try:        
            conn = sql.connect(BaseDatos)
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {table} VALUES (null, ?, ?)", (producto, precio))

            # Guarda los cambios en la base de datos
            conn.commit()

            #Cierra el cursor y la conexión a la base de datos
            cursor.close()
            conn.close()
        except:
             print("El producto ya se encuentra registrado")   

            
#FUNCION PARA ELIMINAR UNA TABLA EN LA PASE DE DATOS          
    def delete_Table(BaseDatos,table):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"""DROP TABLE {table}  """)
        conn.commit()
        conn.close()
        print(f"Se a Eliminado la Tabla de Poructos:{table} Correctamente")


#FUNCION PARA ACTUALIZAR UN PRODUCTO EN LA BASE DE DATOS
    def update(BaseDatos, table, precio, producto):
        try:
            conn = sql.connect(BaseDatos)
            cursor = conn.cursor()
            cursor.execute(f"UPDATE {table} SET precio = ? WHERE producto = ?", (precio, producto))
            conn.commit()
            conn.close()
        except:
             print("El Producto No Existe en la Base de Datos")
        

#FUNCION PARA ELIMINAR TODA LA BASE DE DATOS
    def delete_database():
        pass
        import os
        if os.path.exists(bd.optener_ruta()):
            # Elimina el archivo
            os.remove(bd.optener_ruta())
            print("Base de datos eliminada con éxito")
        else:
            print("No se ha encontrado el archivo de la base de datos")

        
#FUNCION PARA BUSCAR EL PRECIO DE UN PRODUCTO MEDIANTE SU NOMBRE EN LA BASE DE DATOS
    def search_price( BaseDatos, table, producto):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"SELECT precio FROM {table} WHERE producto=?", (producto,))
        precio = cursor.fetchone()[0]
        conn.close()
        return precio


#FUNCION PARA BUSCAR UN PRODUCTO MEDIANDO EL ID DEL MISMO EN LA BASE DE DATOS
    def search_by_id(BaseDatos,table, id):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table} WHERE id=?", (id,))
        id, nombre, precio = cursor.fetchone()
        conn.close()
        return id, nombre, precio

#FUNCION PARA VER TODOS LOS PRODUCTOS EN LA BASE DE DATOS.
    def view_all(BaseDatos,table):
        try:
            conn = sql.connect(BaseDatos)
            consulta = f"SELECT * FROM {table}"
            df = pd.read_sql(consulta, conn)
            dft = tabulate(
            df, headers=["ID","Nombre","Precio"],
            tablefmt="grid",
            showindex=False,
            floatfmt='.2f',
            stralign='center',
            numalign='center')
            print(dft)
        except:
             print("No se puede imprimir la lista porque no se encontro la tabla o no existe")

#FUNCION PARA ELIMINAR UN PRODUCTOS DE LA TABLA DE PRODUCTOS
    def delete_product( BaseDatos, table, producto):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE producto=?", (producto,))
        conn.commit()
        conn.close()
        print("Producto eliminado")

#FUNCION PARA CREAR EL NOMBRE DE LA BASE DE DATOS
    def nombredb(): 
        nombre = input("Ingresa El Nombre de la Base de Datos  Crear: ")
        nombrebd = f"{nombre}.db"
        with open("nombredb.txt", "w") as f:
            f.write(nombrebd)
        return nombrebd
#FUNCION PARA LLAMAR EL NOMBRE DE LA BASE DE DATOS

    def ingresarNombreBD():
        x = open("nombredb.txt")
        BaseDatos = x.read()
        return BaseDatos

#FUNCION PARA CREAR EL NOMBRE DE LA TABLA
    def nombreTable():
        nombreTB = input("Ingresa Nombre de La Tabla a Crear: ")
        with open("nombreTB.txt", "w") as f:
            f.write(nombreTB)
        return nombreTB

#FUNCION PARA LLAMAR EL NOMBRE DE LA TABLA
    def ingresarNombreTB():
        x = open("nombreTB.txt")
        table = x.read()
        return table

#FUNCION PARA ALMACENAR TODOS LOS NOMBRES DE LAS BASE DE DATOS CREADAS
    def historialBD():
        with open("nombredb.txt", "r") as f:
            NombreBD = f.read()

        with open("HistorialBD.txt", "r") as f:
            historialBD = f.read()

        update_historial = (f"{historialBD} \n {NombreBD}")

        with open("HistorialBD.txt", "w") as f:
            f.write(update_historial)

#FUNCION QUE BUSCA LA RUTA DONDE ESTA GUARDADA LA BASE DE DATOS
    def optener_ruta():
        import os
        BaseDatos = bd.ingresarNombreBD()
        # Obtiene la ruta de acceso completa al archivo
        file_ruta = os.path.abspath(BaseDatos)
        return file_ruta

#Intanciando la Clase
bd = Basededatos
