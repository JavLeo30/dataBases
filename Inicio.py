print("""
      ==============================================
      ==========       BIENVENIDO          =========
                AL SISTEMA DE FACTURACION           
      ==========       Py-FACTURE          =========
                ===========================         
                        By: JavLeo
                  Telegram: @JavLeo30 """)



opcion = input("Ingresar como admin: ")

if opcion == "1":
    import admin
elif opcion == "2":
    import operador

