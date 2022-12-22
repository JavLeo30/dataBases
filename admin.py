import sqlite3 as sql
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
while True:

    if comando == "1":
        from basedatos import *
        bd = Basededatos
        BaseDatos = bd.nombredb()
        bd.createDB(BaseDatos)

    elif comando == "2":
        from basedatos import *
        bd.create_Table()

    elif comando == "3":
        from basedatos import *
        bd = Basededatos
        bd.insertRow()

    elif comando == "4":
        from basedatos import *
        bd = Basededatos
        bd.view_all()

    elif comando == "5":
        from basedatos import *
        bd = Basededatos
        bd.update()

    elif comando == "6":
        from basedatos import *
        bd = Basededatos
        bd.delete_product()

    elif comando == "7":
        from basedatos import *
        bd = Basededatos
        bd.delete_Table()

    elif comando == "8":
        from basedatos import *
        bd = Basededatos
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
