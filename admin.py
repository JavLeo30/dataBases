import sqlite3 as sql
from basedatos import *
bd = Basededatos
while True:
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
      bd.create_Table(BaseDatos,bd.nombreTable())

  elif comando == "3":
      bd.insertRow()

  elif comando == "4":
      bd.view_all()

  elif comando == "5":
      bd.update()

  elif comando == "6":
      bd.delete_product()

  elif comando == "7":
      bd.delete_Table()

  elif comando == "8":
      bd.delete_database()

  elif comando == "9":

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


  elif comando == "x":
      print("Fin Del Programa")
      break
