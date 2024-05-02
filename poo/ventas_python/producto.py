from iCrud import ICrud
from utilities import borrarPantalla
from clsJson import JsonFile
import json
import os 
import sys
import time
import random
path, _ = os.path.split(os.path.abspath(__file__))
path=path+"/archivos/products.json"
# print("/")
# print(ruta_absoluta)
# print("/")
# ruta_2 = os.path.split(ruta_absoluta)
# print()
# directorio, nombre_archivo = os.path.split(ruta_absoluta)
# print("/")
# print(directorio)
# print("/")
# print(nombre_archivo)


class CrudClients(ICrud):
    # def __init__(self,fullname) -> None:
    #     self.fullname = fullname
    #     pass        
    def presentar_producto(self,producto):
        return f" Id: {producto['id'] } - Descripcion: {producto['descripcion']} - Precio: {producto['precio']} - Stock:{producto['stock']}"
    #
        
    def create(self):
        Estruc_json_products = {
            "id": 0,
            "descripcion": "",
            "precio": 0,
            "stock": 0
        }
        
        json_file = JsonFile(path)
        data = json_file.read()
        
        while True:
            nombre = input("Ingrese el nombre del producto: ")
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            
            if any(produc["descripcion"] == nombre for produc in data):
                print("El nombre ya existe en los datos. Por favor, ingrese un nombre diferente.")
            else:
                print("El nombre es válido y único.")
                Estruc_json_products["descripcion"] = nombre
                break
            
        Estruc_json_products["id"] = len(data) + 1
        Estruc_json_products["precio"] = float(input("Ingrese el precio del producto: ")) 
        Estruc_json_products["stock"] = random.randint(100, 2000)
        borrarPantalla()
           
        data.append(Estruc_json_products)
        json_file.save(data)
    #
    def update(self):
        json_file = JsonFile (path)
        
        productos = json_file.read()
        
        print("Lista de clientes: ")
        list(map(lambda producto: print(self.presentar_producto(producto)), productos))
        print()
        for i in range(3, 0, -1):
            sys.stdout.write("\rTiempo restante: {} segundos".format(i))
            sys.stdout.flush()
            time.sleep(1)
        #    
        sys.stdout.write("\r¡Tiempo agotado de ver los usuarios!")
        time.sleep(1.2)
        borrarPantalla()
        
        id_producto = input("Ingrese el 'Id' del producto que desea actualizar:")    
        while (True):
            producto_encontrado = json_file.find("id",int(id_producto))
            
            if (producto_encontrado) :
                producto = producto_encontrado[0]
                print()
                print("producto encontrado:")
                print("Descripcion:", producto["descripcion"])
                print("Precio:", producto["precio"])
                print("Stock:", producto["stock"])
                print()
                break
            else:
                print("No se encontró ningún producot con el 'Id' proporcionado.")
                print("Ingrese de nuevo el dni: ")
                id_producto = input()  
            #        
        #
        #print(cliente)
        #print(clientes)

        print("Desea modificarlo al usuario: ",id_producto)
        print("Ingrese s/n:")    
        Op = input()
        while (True):
            if (Op.lower() =="s"):
                producto["descripcion"] = input("Ingrese el nuevo nombre del producto: ")
                producto["precio"] = float(input("Ingrese el el precio: "))
                producto["stock"] = int(random.randint(100,2000))
                for Indice,valor in enumerate(productos):
                    if valor["id"] == int(id_producto) :
                        productos[Indice] = producto
                        break
                    #
                #       
                json_file.save(productos)
                print("Datos del producto actualizados correctamente.")
                break
            elif  (Op.lower() =="n"):
                print("Ok, Se lo dejara tal cual esta")
                break
            else:
                print("Error: Ingrese 's' para confirmar la modificación o 'n' para cancelar.")

                Op = input() 
            #
        #   
    #    
    def delete(self):
        
            
        json_file = JsonFile (path)
        
        productos = json_file.read()
            
        print("Lista de producto: ")
        list(map(lambda producto: print(self.presentar_producto(producto)), productos))
        print()
        for i in range(3, 0, -1):
            sys.stdout.write("\rTiempo restante: {} segundos".format(i))
            sys.stdout.flush()
            time.sleep(1)
        #    
        sys.stdout.write("\r¡Tiempo agotado de ver los prodcutos!")
        time.sleep(1.2)
        borrarPantalla()
        
        id_producto = input("Ingrese el 'Id' del producto que desea Eliminar:")    
        while (True):
            producto_encontrado = json_file.find("id",int(id_producto))
            
            if (producto_encontrado) :
                producto = producto_encontrado[0]
                print()
                print("Producto encontrado:")
                print("Descripcion:", producto["descripcion"])
                print("Precio:", producto["precio"])
                print("Stock:", producto["stock"])
                print()
                break
            else:
                print("No se encontró ningún producto con el Id proporcionado.")
                print("Ingrese de nuevo el id: ")
                id_producto = input() 
            #    
        #                
        for prod_ in productos:
            print(prod_)
            if prod_.get("id") == int(id_producto):
                productos.remove(prod_)
                break
            #
        #    
        json_file.save(productos)
    #      
    def consult(self):
        producto = JsonFile(path).read()
        list(map(lambda producto: print(self.presentar_producto(producto)), producto))

        


objeto_crud_products = CrudClients()
#objeto_crud_products.create()
#objeto_crud_products.update()

objeto_crud_products.delete()
#objeto_crud_products.consult()

# arr=CrudClients
# arr.create()    