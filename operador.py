import json
import pandas as pd
import datetime
import os

filename = "base_datos.json"
data = open(filename, "r")
data2 = json.loads(data.read())

#lista para anexar cada producto a la factura

#Codigo general para la ejecucion del momento de Facturar porducto.
#==================================================================

            

#Funcion para Imprimir factura Final
def imprimir():
    
    opcion = str.upper(input("Imprimir Factura Y/N : "))
    if opcion == "Y":
        df=pd.DataFrame()
        print(df)
    else:
        print ("Que tenga Buen dia")
    
    

    
#Clase para calcular precio del producto y costo a valor a pagar.


class Calcular():
    
    def __init__(self,cantida,precio):
        self.cantida = cantida
        self.precio  = precio
      
        
    def calculo(self):
        return self.cantida * self.precio

    
    def total_pagar(self,):
        
        total_pagar =  + (self.cantida * self.precio)
        total_pagar = round(total_pagar)
        return total_pagar
    
    
#Clase para ingresar los datos del cliente en la factura y base de datos
class Cliente:
    
    def __init__(self,dni,nombre,apellido,direccion):
        self.dni       = dni
        self.nombre    = nombre
        self.apellido  = apellido
        self.direccion = direccion
    
    def __str__(self):
        return """
    DNI: {}
    Nombre: {} 
    Apellido: {}
    Direccion: {}""".format(self.dni,self.nombre,self.apellido,self.direccion)

#Clase Factura

class Factura():            

    def id_factura(self):
        data = "data_facturas.json" 
        with open(data, "r") as f:
            data=json.load(f)
            data=dict(data)

            key=data.keys()
            self.result = max(key, default=0)
            
            self.numero = self.result
            self.numero += 1
            
        return self.numero

        
    
ident = Factura()
identificar = ident.id_factura()

class Data_factura():
    
    def __init__(self,producto,peso,p_producto,costo):
        
        self.producto   = producto
        self.peso       = peso
        self.p_producto = p_producto
        self.costo      = costo
        
        
    def __dict__(self):

        #return """ #Factura: {} Producto: {} Cantida: {} Precio_Unit: {} TOTAL: {} """.format(self.id,self.producto,self.peso,self.p_producto,self.costo)
        return {"Productos": self.producto, "Cantida": self.peso, "Precio_Unit": self.p_producto, "TOTAL": self.costo}
    
    

class Productos():
    
    lista_producto = []
    
    def lista(self,lista_producto=[]):
        self.Factura_end = lista_producto
        
    def agregar(self,impresion):
        self.Factura_end.append(impresion)

    def mostrar(self):
        for p in self.Factura_end:
            print(p)
               
    def imprimir(self):
        df=pd.DataFrame(self.Factura_end)
        return df

# total = Calcular(10,10)
# print(total.calculo())
