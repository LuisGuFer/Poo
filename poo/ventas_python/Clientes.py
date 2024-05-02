from iCrud import ICrud
from utilities import borrarPantalla
from clsJson import JsonFile
import json
import os 
import sys
import time
import random
path, _ = os.path.split(os.path.abspath(__file__))
path=path+"/archivos/clients.json"
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
    def presentar_cliente(self,cliente):
        return f" DNI: {cliente['dni'] } - Nombre: {cliente['nombre']} - Apellido: {cliente['apellido']} - Valor{cliente['valor']}"

    def validar_cedula(func):
        def wrapper(*args, **kwargs):
            
            id_persona = func(*args, **kwargs)
            codigo_provincia = id_persona[:2]
            while codigo_provincia not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]:
                id_persona = func(*args,**kwargs)
                codigo_provincia = id_persona[:2]
            return id_persona
        return wrapper
    #

    @validar_cedula
    def generar_id(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])  
    #  
    def create(self):
        
        Estruc_json_clients={
            "dni":"",
            "nombre":"",
            "apellido":"",
            "valor":0
        }
        
        with open(path, "r") as File_Json:
            data = json.load(File_Json)
            # print(Id_Json_Cliente)
            nombre_existe = False
            while (True):
                nombre = input("Ingrese el nombre: ")
                if not (nombre):
                    print("El nombre no puede estar vacío.")
                    continue
                #
                if any(cliente["nombre"] == nombre for cliente in data):
                    print("El nombre ya existe en los datos. Por favor, ingrese un nombre diferente.")
                else:
                    print("El nombre es válido y único.")
                    Estruc_json_clients["nombre"] = nombre
                    break
                #
            #    
            Estruc_json_clients["dni"] = str(self.generar_id())
            Estruc_json_clients["valor"] = random.randint(100,2000) 
            Estruc_json_clients["apellido"] = input("Ingrese el apellido: ")
            borrarPantalla()
        #        
        data.append(Estruc_json_clients)
        with open(path, "w") as File_Json:
            json.dump(data, File_Json, indent = 2)
        #    
    #
    def update(self):
        json_file = JsonFile (path)
        
        clientes = json_file.read()
        
        print("Lista de clientes: ")
        list(map(lambda cliente: print(self.presentar_cliente(cliente)), clientes))
        print()
        for i in range(3, 0, -1):
            sys.stdout.write("\rTiempo restante: {} segundos".format(i))
            sys.stdout.flush()
            time.sleep(1)
        #    
        sys.stdout.write("\r¡Tiempo agotado de ver los usuarios!")
        time.sleep(1.2)
        borrarPantalla()
        
        dni_cliente = input("Ingrese el DNI del cliente que desea actualizar:")    
        while (True):
            cliente_encontrado = json_file.find("dni",dni_cliente)
            
            if (cliente_encontrado) :
                cliente = cliente_encontrado[0]
                print()
                print("Cliente encontrado:")
                print("Nombre:", cliente["nombre"])
                print("Apellido:", cliente["apellido"])
                print("Valor:", cliente["valor"])
                print()
                break
            else:
                print("No se encontró ningún cliente con el DNI proporcionado.")
                print("Ingrese de nuevo el dni: ")
                dni_cliente = input()  
            #        
        #
        #print(cliente)
        #print(clientes)

        print("Desea modificarlo al usuario: ",dni_cliente)
        print("Ingrese s/n:")    
        Op = input()
        while (True):
            if (Op.lower() =="s"):
                cliente["nombre"] = input("Ingrese el nuevo nombre del cliente: ")
                cliente["apellido"] = input("Ingrese el nuevo apellido del cliente: ")
                cliente["valor"] = int(random.randint(100,2000))
                for Indice,valor in enumerate(clientes):
                    if valor["dni"] == dni_cliente :
                        clientes[Indice] = cliente
                        break
                    #
                #       
                print(clientes)
                json_file.save(clientes)
                print("Datos del cliente actualizados correctamente.")
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
        with open(path, "r") as json_file:
            
            json_file = JsonFile (path)
        
            clientes = json_file.read()
            
            print("Lista de clientes: ")
            for cliente in clientes :
                print("DNI:", cliente["dni"], "- Nombre:", cliente["nombre"], "- Apellido:", cliente["apellido"], "- Valor",cliente["valor"])
            #
            print()
            for i in range(3, 0, -1):
                sys.stdout.write("\rTiempo restante: {} segundos".format(i))
                sys.stdout.flush()
                time.sleep(1)
            #    
            sys.stdout.write("\r¡Tiempo agotado de ver los usuarios!")
            time.sleep(1.2)
            borrarPantalla()
            
            dni_cliente = input("Ingrese el DNI del cliente que desea Eliminar:")    
            while (True):
                cliente_encontrado = json_file.find("dni",dni_cliente)
                
                if (cliente_encontrado) :
                    cliente = cliente_encontrado[0]
                    print()
                    print("Cliente encontrado:")
                    print("Nombre:", cliente["nombre"])
                    print("Apellido:", cliente["apellido"])
                    print("Valor:", cliente["valor"])
                    print()
                    break
                else:
                    print("No se encontró ningún cliente con el DNI proporcionado.")
                    print("Ingrese de nuevo el dni: ")
                    dni_cliente = input() 
                #     
            #                
            for usuario in clientes:
                print(usuario)
                if usuario.get("dni") == dni_cliente:
                    clientes.remove(usuario)
                    break
                #
            #    
        
            json_file.save(clientes)
        #
    #        
    def consult(self):
        cliente = JsonFile(path).read()
        list(map(lambda cliente: print(self.presentar_cliente(cliente)), cliente))

        
objeto_crud_clients = CrudClients()
# objeto_crud_clients.update()
# objeto_crud_clients.consult()
objeto_crud_clients.create()
# arr=CrudClients
# arr.create()    