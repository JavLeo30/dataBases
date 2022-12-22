import sqlite3 as sql
import pandas as pd

class Basededatos():
    
#FUNCION PARA CREAR UNA BASE DE DATOS
    def createDB(self,BaseDatos):
        conn = sql.connect(BaseDatos)
        conn.commit()
        conn.close()
        return BaseDatos

#FUNCION PARA CREAR UNA TABLA EN LA BASE DE DATOS
    def create_Table(self,BaseDatos,table):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table}
                    (id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0,
                    Producto TEXT UNIQUE,
                    Precio REAL) """)       
        conn.commit()
        conn.close()
        return table

#FUNCION PARA INSERTAR UN NUEVO PRODUCTO Y SU PRECIO EN LA BASE DE DATOS
    def insertRow(self,BaseDatos,table, producto, precio):
        try:        
            conn = sql.connect(BaseDatos)
            cursor = conn.cursor()

            # Asigna el valor a la variable 'insert_query' antes de utilizarla
            insert_query = f"INSERT INTO {table} VALUES (null, ?, ?)"

            # Ejecuta la consulta con placeholders
            cursor.execute(insert_query, (producto, precio))

            # Guarda los cambios en la base de datos
            conn.commit()

            #Cierra el cursor y la conexión a la base de datos
            cursor.close()
            conn.close()
        except:
            print("El producto ya se encuentra registrado")   

            
#FUNCION PARA ELIMINAR UNA TABLA EN LA PASE DE DATOS          
    def delete_Table(self,BaseDatos,table):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"""DROP TABLE {table}  """)
        conn.commit()
        conn.close()
        


#FUNCION PARA ACTUALIZAR UN PRODUCTO EN LA BASE DE DATOS
    def update(self, BaseDatos, table, precio, producto):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {table} SET precio = ? WHERE producto = ?", (precio, producto))
        conn.commit()
        conn.close()
        

#FUNCION PARA ELIMINAR TODA LA BASE DE DATOS
    def delete_database(self,BaseDatos,basededatos):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"DROP DATABASE {basededatos}")
        conn.commit()
        conn.close()

        
#FUNCION PARA BUSCAR EL PRECIO DE UN PRODUCTO MEDIANTE SU NOMBRE EN LA BASE DE DATOS
    def search_price(self, BaseDatos, table, producto):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"SELECT precio FROM {table} WHERE producto=?", (producto,))
        precio = cursor.fetchone()[0]
        conn.close()
        return precio


#FUNCION PARA BUSCAR UN PRODUCTO MEDIANDO EL ID DEL MISMO EN LA BASE DE DATOS
    def search_by_id(self,BaseDatos,table, id):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table} WHERE id=?", (id,))
        id, nombre, precio = cursor.fetchone()
        conn.close()
        return id, nombre, precio

#FUNCION PARA VER TODOS LOS PRODUCTOS EN LA BASE DE DATOS.
    def view_all(self,BaseDatos,table):
        conn = sql.connect(BaseDatos)
        consulta = f"SELECT * FROM {table}"

        df = pd.read_sql(consulta, conn)
        print(df)


#FUNCION PARA ELIMINAR UN PRODUCTOS DE LA TABLA DE PRODUCTOS
    def delete_product(self, BaseDatos, table, producto):
        conn = sql.connect(BaseDatos)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE producto=?", (producto,))
        conn.commit()
        conn.close()


#FUNCION PARA CREAR EL NOMBRE DE LA BASE DE DATOS
    def nombredb(self,): 
        nombre = input("Ingresa El Nombre de la Base de Datos  Crear: ")
        nombrebd = f"{nombre}.db"
        with open("nombredb.txt", "w") as f:
            f.write(nombrebd)
        return nombrebd
#FUNCION PARA LLAMAR EL NOMBRE DE LA BASE DE DATOS

    def ingresarNombreBD(self,):
        x = open("nombredb.txt")
        BaseDatos = x.read()
        return BaseDatos

#FUNCION PARA CREAR EL NOMBRE DE LA TABLA
    def nombreTable(self,):
        nombreTB = input("Ingresa Nombre de La Tabla a Crear: ")
        with open("nombreTB.txt", "w") as f:
            f.write(nombreTB)

#FUNCION PARA LLAMAR EL NOMBRE DE LA TABLA
    def ingresarNombreTB(self):
        x = open("nombreTB.txt")
        table = x.read()
        return table

#FUNCION PARA ALMACENAR TODOS LOS NOMBRES DE LAS BASE DE DATOS CREADAS
    def historialBD(self):
        with open("nombredb.txt", "r") as f:
            NombreBD = f.read()

        with open("HistorialBD.txt", "r") as f:
            historialBD = f.read()

        update_historial = (f"{historialBD} \n {NombreBD}")

        with open("HistorialBD.txt", "w") as f:
            f.write(update_historial)


# BaseDatos = bd.nombredb()
# bd.createDB(BaseDatos)
# table = bd.ingresarNombreTB()


                                           #//Usado para la administracion del sistema

# bd.createTable(BaseDatos, table)                                 #//Usado para la administracion del sistema

# bd.insertRow(BaseDatos,table,"pera", 1.235)                      #//Usado para la administracion del sistema

# bd.delete_Table(BaseDatos,table)                                #//Usado para la administracion del sistema

# bd.update(BaseDatos, table, 5, "pera")                         #//Usado para la administracion del sistema

# bd.delete_database(BaseDatos)                                  #//Usado para la administracion del sistema

# x = bd.search_price(BaseDatos, table, "pera")                  #//Usado para la caja de facturacion
# print(x)

# bd.view_all(BaseDatos,table)                                   #//Usado para la administracion del sistema  

# data = [bd.search_by_id(BaseDatos,table,(1))]                  #//Usado para la caja de facturacion y admistracion del sistema
# df = pd.DataFrame(data, columns=['ID', 'Nombre', 'Precio'])
# print(df)

