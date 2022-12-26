import sqlite3 as sql
from basedatos import *
import os
def administracion():
      
  bd = Basededatos
  while True:
    os.system("cls")
    print("""
    ----------------Comandos Disponiles-------------------------
    --    1 = Crear Base de Datos.                            --
    --    2 = Crear Tabla de Productos (id,Name,Precio).      --
    --    3 = Ingresar Porducto a la Base de Datos            --
    --    4 = Ver la lista de productos Precio y Id.          --
    --    5 - Actualizar Precio de  Producto                  --
    --    6 = Elimina un Producto de la Data.                 --
    --    7 = Eliminar la Lista de Productos                  --
    --    8 = Elimina Toda La Data.                           --
    --    9 = Muestra el menu de Opciones de Comandos         --
    --    x = Finaliza el Programa                            --
    ------------------------------------------------------------""")
    comando = (input("Ingrese una Opncion del Menu de Comandos: "))

    if comando == "1":
        
        BaseDatos = bd.nombredb()
        bd.createDB(BaseDatos)

    elif comando == "2":
        BaseDatos = bd.ingresarNombreBD()
        bd.create_Table(BaseDatos,bd.nombreTable())

    elif comando == "3":
        product   = str(input("Nombre Del Producto: ")).capitalize
        price     = float(input("Valor Del Producto: "))
        table     = bd.ingresarNombreTB()
        BaseDatos = bd.ingresarNombreBD()
        bd.insertRow(BaseDatos,table,product,price)

    elif comando == "4":
        table     = bd.ingresarNombreTB()
        BaseDatos = bd.ingresarNombreBD()
        bd.view_all(BaseDatos,table)

    elif comando == "5":
        product   = str(input("Nombre Del Producto: ")).capitalize
        price     = float(input("Nuevo Valor Del Producto: "))
        table     = bd.ingresarNombreTB()
        BaseDatos = bd.ingresarNombreBD()
        bd.update(BaseDatos,table,price,product)
        print(f"""
        El Precio de {product} se Actualizo Correctamente
        el Precio de {product} es: {price}""")

    elif comando == "6":
        product   = str(input("Nombre Del Producto a Eliminar: ")).capitalize
        BaseDatos = bd.ingresarNombreBD()
        table     = bd.ingresarNombreTB()
        bd.delete_product(BaseDatos,table,product)

    elif comando == "7":
        BaseDatos = bd.ingresarNombreBD()
        table     = bd.ingresarNombreTB()
        bd.delete_Table(BaseDatos,table)

    elif comando == "8":
        bd.delete_database()

    elif comando == "9":
        pass


    elif comando == "x" or "X":
        print("Fin Del Programa")
        break

