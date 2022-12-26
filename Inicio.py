import os
while True:
    os.system("cls")
    print("""
        ==============================================
        ==========       BIENVENIDO          =========
                    AL SISTEMA DE FACTURACION           
        ==========       Py-FACTURE          =========
                    ===========================         
                            By: JavLeo
                    Telegram: @JavLeo30 """)


    print("""
        --------------Comandos Disponiles-----------
        --  1 = Iniciar En Modo Administrador.    --
        --  2 = Iniciar En Modo Operador (CAJA).  --
        --  x = Finaliza el Programa              --
        --------------------------------------------""")
    opcion = input("Como Desea Iniciar: ")

    if opcion == "1":
        from admin import administracion
        administracion()

    elif opcion == "2":
        import operador
    
    elif opcion == "x" or "X":
        print("Programa Finalizado")
        break

