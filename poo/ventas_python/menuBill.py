from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os,sys,random
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
    def presentar_cliente(self,cliente):
        return f" DNI: {cliente['dni'] } - Nombre: {cliente['nombre']} - Apellido: {cliente['apellido']} - Valor{cliente['valor']}"
    #
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
        Estruc_json_clients = {
            "dni": "",
            "nombre": "",
            "apellido": "",
            "valor": 0
        }

        jsonfile = JsonFile(path+'/archivos/clients.json')
        data = jsonfile.read()
        while (True):
            nombre = input("Ingrese el nombre: ")
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            if any(cliente["nombre"] == nombre for cliente in data):
                print("El nombre ya existe en los datos. Por favor, ingrese un nombre diferente.")
            else:
                print("El nombre es válido y único.")
                Estruc_json_clients["nombre"] = nombre
                break
            #
        #    
        Estruc_json_clients["dni"] = str(self.generar_id())
        Estruc_json_clients["valor"] = random.randint(100, 2000)
        Estruc_json_clients["apellido"] = input("Ingrese el apellido: ")
        borrarPantalla()

        data.append(Estruc_json_clients)
        jsonfile.save(data)
    #    
    def update(self):
        json_file = JsonFile(path+'/archivos/clients.json')
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
        while True:
            cliente_encontrado = json_file.find("dni", dni_cliente)
            if cliente_encontrado:
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
        print("Desea modificarlo al usuario: ", dni_cliente)
        print("Ingrese s/n:")
        op = input()
        while True:
            if op.lower() == "s":
                cliente["nombre"] = input("Ingrese el nuevo nombre del cliente: ")
                cliente["apellido"] = input("Ingrese el nuevo apellido del cliente: ")
                cliente["valor"] = int(random.randint(100, 2000))
                for indice, valor in enumerate(clientes):
                    if valor["dni"] == dni_cliente:
                        clientes[indice] = cliente
                        break
                print(clientes)
                json_file.save(clientes)
                print("Datos del cliente actualizados correctamente.")
                break
            elif op.lower() == "n":
                print("Ok, Se lo dejara tal cual esta")
                break
            else:
                print("Error: Ingrese 's' para confirmar la modificación o 'n' para cancelar.")
                op = input()
            #
        #
    #        
    def delete(self):
        json_file = JsonFile(path+'/archivos/clients.json')
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
            #print(usuario)
            if usuario.get("dni") == dni_cliente:
                clientes.remove(usuario)
                break
            #
        #
        while (True) :
            op = input("¡Seguro que quieres eliminar este usuario...!\nIngrese s/n:\n")
            if (op.lower() == "s"):
                json_file.save(clientes)
                print("USUARIO ELIMINADO EXITOSAMENTE")
                time.sleep(1)
                break

            elif  (op.lower() == "n"):
                print("¡NO SE ELIMINARA NINGUN USUARIO!")
                time.sleep(1)
                break
            else:
                print("Error: Ingrese 's' para confirmar la modificación o 'n' para cancelar.")
                op = input()
            #
        #        
    #   
    def consult(self):
        json_file = JsonFile(path+'/archivos/clients.json')
        clientes = json_file.read()        
        list(map(lambda clientes: print(self.presentar_cliente(clientes)), clientes))
        

class CrudProducts(ICrud):
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
        
        json_file = JsonFile(path+'/archivos/products.json')
        data = json_file.read()
        
        while True:
            nombre = input("Ingrese el nombre del producto: ")
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            #
            if any(produc["descripcion"] == nombre for produc in data):
                print("El nombre ya existe en los datos. Por favor, ingrese un nombre diferente.")
            else:
                print("El nombre es válido y único.")
                Estruc_json_products["descripcion"] = nombre
                break
            #
        #    
        precio = None
        while precio is None:
            try:
                precio = float(input("Ingrese el nuevo precio del producto: "))
                break
            except ValueError:
                print("Error: Por favor, ingrese un número para el precio.")
                continue
            #
        Estruc_json_products["id"] = len(data) + 1
        Estruc_json_products["precio"] = precio
        Estruc_json_products["stock"] = random.randint(100, 2000)
        data.append(Estruc_json_products)
        json_file.save(data)
        print("El producto se ha creado")
        time.sleep(2)        
        borrarPantalla()
    #
    def update(self):
        json_file = JsonFile (path+'/archivos/products.json')
        
        productos = json_file.read()
        
        print("Lista de clientes: ")
        list(map(lambda producto: print(self.presentar_producto(producto)), productos))
        print()
        for i in range(3, 0, -1):
            sys.stdout.write("\rTiempo restante: {} segundos".format(i))
            sys.stdout.flush()
            time.sleep(1)
        #    
        sys.stdout.write("\r¡Tiempo agotado de ver los producto!")
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
                print("Ingrese de nuevo el id: ")
                id_producto = input()  
            #        
        #
        #print(cliente)
        #print(clientes)

        print("Desea modificarlo al usuario: ",id_producto)
        print("Ingrese s/n:")    
        Op = input()
        while True:
            if (Op.lower() == "s"):
                nombre = input("Ingrese el nuevo nombre del producto: ")
                precio = None
                while precio is None:
                    try:
                        precio = float(input("Ingrese el nuevo precio del producto: "))
                    except ValueError:
                        print("Error: Por favor, ingrese un número para el precio.")
                        continue
                    #
                # 
                producto["descripcion"] = nombre
                producto["precio"] = precio
                # Actualizar el stock del producto
                producto["stock"] = random.randint(100, 2000)
                
                for indice, valor in enumerate(productos):
                    if valor["id"] == int(id_producto):
                        productos[indice] = producto
                        break
                    #
                #    
                json_file.save(productos)
                print("Datos del producto actualizados correctamente.")
                time.sleep(1)
                break
            elif (Op.lower() == "n"):
                print("Datos del producto actualizados correctamente.")
                break
            else:
                print("Error: Ingrese 's' para confirmar la modificación o 'n' para cancelar.")
                Op = input() 
            #
        #   
    #    
    def delete(self):
        
            
        json_file = JsonFile (path+'/archivos/products.json')
        
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
        Op = input("¡SEGURO QUE QUIERES ELIMNAR ESTE PRODUCTO!\n")
        while True:
            if Op.lower() == "s":
                print("Se eliminara el producto")             
                for prod_ in productos:
                    print(prod_)
                    if prod_.get("id") == int(id_producto):
                        productos.remove(prod_)
                        break
                    #
                #
            elif Op.lower() == "n":
                print("Ok, No se eliminara el prodcuto")
                time.sleep(1)
                break
            else:
                Op = input("Error: Ingrese 's' para eliminar el producto o 'n' para cancelar.\n") 
            #
            time.sleep(1)    
        json_file.save(productos)
    #      
    def consult(self):
        producto = JsonFile(path+'/archivos/products.json').read()
        print("Lista de Productos")
        list(map(lambda producto: print(self.presentar_producto(producto)), producto))
        time.sleep(3)
    #    

class CrudSales(ICrud):
    def create(self):
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cedula:")
        dni=validar.solo_numeros("Error: Solo numeros",23,6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print("Cliente no existe")
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(green_color+"*"*90+reset_color) 
        gotoxy(5,9);print(purple_color+"Linea") 
        gotoxy(12,9);print("Id_Articulo") 
        gotoxy(24,9);print("Descripcion") 
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line)
            id=int(validar.solo_numeros("Error: Solo numeros",15,9+line))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(24,9+line);print("Producto no existe")
                time.sleep(1)
                gotoxy(24,9+line);print(" "*20)
            else:    
                prods = prods[0]
                product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros",49,9+line))
                gotoxy(59,9+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(76,4);print(round(sale.subtotal,2))
                gotoxy(76,5);print(round(sale.discount,2))
                gotoxy(76,6);print(round(sale.iva,2))
                gotoxy(76,7);print(round(sale.total,2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(green_color+"✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            ult_invoices = invoices[-1]["factura"]+1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print("🤣 Venta Cancelada 🤣"+reset_color)    
        time.sleep(2)    
    #
    def mostrar_facturas(self):
         # Leer el archivo de facturas
        json_file = JsonFile(path+'/archivos/invoices.json')
        # print(json_file)
        facturas = json_file.read()
        # Mostrar todas las facturas disponibles
        # print(facturas)

        gotoxy(2, 6); print(green_color + "*" * 100 )
        gotoxy(35,7 ); print(blue_color+"Lista de Facturas")
        gotoxy(2,8); print(green_color + "*" * 100 + reset_color)
        gotoxy(1,9);print(blue_color+"Factura #") 
        gotoxy(15,9);print(blue_color+"Cliente") 
        gotoxy(28,9);print(blue_color+"Fecha") 
        gotoxy(39,9);print(blue_color+"Cantidad") 
        gotoxy(52,9);print(blue_color+"Subtotal")
        gotoxy(65,9);print(blue_color+"Descuento")
        gotoxy(78,9);print(blue_color+"IVA")
        gotoxy(85,9);print(blue_color+"Total")
        gotoxy(96,9);print(blue_color+"Detalle:")
        linea=10
        for factura in facturas:
            cantidad_total = sum(detalle["cantidad"] for detalle in factura["detalle"])
            # print(green_color+"*"*90+reset_color)
            gotoxy(4,linea);print(factura["factura"])
            gotoxy(12,linea);print(factura["cliente"])
            gotoxy(26,linea);print(factura["Fecha"])
            gotoxy(54,linea);print(factura["subtotal"])
            gotoxy(67,linea);print(round(factura["descuento"],1))
            gotoxy(78,linea);print(round(factura["iva"],1))
            gotoxy(85,linea);print(factura["total"])
            for detalle in factura["detalle"]:
                detalle["cantidad"] = cantidad_total
                gotoxy(41,linea);print(detalle["cantidad"] )
            #    
            linea += 1            
            #print(linea)
        #    
        for factura in facturas:
            # Imprimir el encabezado del detalle de la factura
            gotoxy(2, linea); print(blue_color+"Detalle de los productos comprados por el cliente de la Factura #", factura["factura"])
            linea += 1
            # Imprimir los encabezados de las columnas del detalle
            gotoxy(2, linea); print(green_color+"Producto")
            gotoxy(30, linea); print(green_color+"Precio")
            linea += 1
            # Iterar sobre los detalles de la factura e imprimir cada producto
            for detalle in factura["detalle"]:
                gotoxy(2, linea); print(detalle["poducto"])  
                gotoxy(30, linea); print(detalle["precio"])
                linea += 1
            #    
            # Separación entre las facturas
            linea += 1
            print(green_color + "*" * 100+reset_color )
        #    
    #    
    def update(self):
        # Pedir al usuario que ingrese el ID de la factura a modificar
        json_file = JsonFile(path+'/archivos/invoices.json')
        json_file_p = JsonFile(path+'/archivos/products.json')
        facturas = json_file.read()
        list_prod = json_file_p.read()
        self.mostrar_facturas()
        for i in range(8, 0, -1):
            sys.stdout.write(red_color+"\rTiempo restante: {} segundos".format(i))
            sys.stdout.flush()
            time.sleep(1)
        #    
        sys.stdout.write("\r¡Tiempo agotado de ver las facturas!"+green_color)
        time.sleep(1.2)
        borrarPantalla()
        factura_id = None
        while factura_id is None or not isinstance(factura_id, int):
            factura_input = input(green_color+"Ingrese el ID de la factura que desea modificar (debe ser un número entero): ")
            try:
                factura_id = int(factura_input)
            except ValueError:
                print(red_color+"Por favor, ingrese un número entero válido.")
            #
        #        
        factura = next((f for f in facturas if f["factura"] == factura_id), None)
        #Factura_encontrado = json_file.find("id",factura_id)
        #print(factura)
        if factura:
            while True:
                confirmacion = input(green_color+"¿Desea modificar esta factura? (s/n): ").lower()
                if confirmacion == "s":
                    while True:
                        opcion = input(green_color+"¿Qué desea modificar (prodcuto/cantidad)? (s/n) s-->'Nombre del producto' n--> 'cantidad':\n").lower()
                        if opcion == "s":
                            # Modificar el nombre del producto
                            borrarPantalla()
                            pro = 1
                            for detalle in factura["detalle"]:
                                print(green_color+"*"*50+reset_color)
                                print(blue_color+"Numero de producto: ", pro, "#")
                                print("Nombre del producto: ", detalle["poducto"])
                                print("Precio: ", detalle["precio"])
                                print("Cantidad:", detalle["cantidad"],""+reset_color)
                                print(green_color+"*"*50+reset_color)
                                pro += 1
                            while True:
                                nume_prod = int(input(green_color+"Ingresa el numero de producto: "))
                                
                                for indice, valor in enumerate(factura["detalle"]):
                                    if (nume_prod - 1) == indice:
                                        while True:
                                            nuevo_nombre = input("Ingrese el nuevo nombre del producto: "+reset_color)
                                            function  = lambda name : any (nuevo_nombre.lower() == lis["descripcion"].lower() for lis in json_file_p)
                                            Boo = function(json_file_p)
                                            if Boo:
                                                break
                                            else:
                                                print("¡NOMBRE NO ENCONTRADO EN LA LISTA DE PRDOUCTOS!")
                                            #
                                        #        
                                        factura["detalle"][indice]["poducto"] = nuevo_nombre.lower()
                                        print(purple_color+"El nombre del producto ha sido modificado exitosamente."+reset_color)
                                        break
                                else:
                                    print(red_color+"Número de producto no válido."+reset_color)
                                    continue  
                                break   
                            #
                            json_file.save(facturas)
                            break
                        elif opcion == "n":
                            # Modificar la cantidad del producto
                            pro = 1
                            for detalle in factura["detalle"]:
                                print(green_color+"*"*50+reset_color)
                                print(blue_color+"Numero de producto: ", pro, "#")
                                print("Nombre del producto: ", detalle["poducto"])
                                print("Precio: ", detalle["precio"])
                                print("Cantidad:", detalle["cantidad"],""+reset_color)
                                print(green_color+"*"*50+ reset_color)
                                pro += 1
                            #
                                
                            while True:
                                try:
                                    nume_prod = int(input(green_color+"Ingresa el número de producto: "))
                                    if nume_prod < 1 or nume_prod > len(factura["detalle"]):
                                        print(red_color+"Número de producto no válido. Por favor, ingresa un número dentro del rango."+reset_color)
                                        continue
                                    #
                                    nueva_cantidad = int(input(green_color+"Ingrese la nueva cantidad: "+reset_color))
                                    for indice, detalle in enumerate(factura["detalle"]):
                                        if (nume_prod - 1) == indice:
                                            factura["detalle"][indice]["cantidad"] = nueva_cantidad
                                            # Recalcular subtotal, descuento, iva y total
                                            for nom_pr in list_prod:
                                                if ((nom_pr["descripcion"]).lower() == (factura["detalle"][indice]["poducto"]).lower()):
                                                    
                                                    #print(nom_pr["descripcion"])
                                                    #print(factura["detalle"][indice]["poducto"])
                                                    factura["detalle"][indice]["precio"] = nom_pr["precio"]
                                                    #print(factura)
                                                    break
                                                #
                                            #    
                                            subtotal = sum(det["precio"] * det["cantidad"] for det in factura["detalle"])
                                            descuento = subtotal * 0.10
                                            iva = (subtotal - descuento) * 0.12
                                            total = subtotal - descuento + iva
                                            factura["subtotal"] = round(subtotal, 2)
                                            factura["descuento"] = round(descuento, 2)
                                            factura["iva"] = round(iva, 2)
                                            factura["total"] = round(total, 2)
                                            print(purple_color+"La cantidad del producto ha sido modificada exitosamente."+reset_color)
                                            # Guardar los cambios y salir del bucle
                                            json_file.save(facturas)
                                            break
                                        #
                                    else:
                                        print(red_color+"¡NUMERO DE PRODUCTO NO VALIDO!")
                                        continue
                                except ValueError:
                                    print(red_color+"¡ENTRADA NO VALIDA!. POR FAVOR, INGRESA NUMERO ENTERO."+reset_color)
                                    continue
                                else:
                                    break
                                #
                            # 
                        else:
                            print(red_color+"¡OPCION NO VALIDA!"+reset_color)                  
                elif confirmacion == "n":
                    print(red_color+"OPERACION CANCELADA."+reset_color)
                    break
                else:
                    print(red_color+"¡OPCINO NO VALIDA!."+reset_color)
                #
            #              
        else:
            print(red_color+"No se encontró ninguna factura con el ID proporcionado."+reset_color)
        #
    #
    def delete(self) :
        json_file = JsonFile(path+'/archivos/invoices.json')
        facturas =json_file.read()
        # Buscar la factura con el ID especificado
        factura_id = None
        while factura_id is None or not isinstance(factura_id, int):
            factura_input = input(green_color+"Ingrese el ID de la factura que desea eliminar: ")
            try:
                factura_id = int(factura_input)
            except ValueError:
                print(red_color+"POR FAVOR, INGREEO UN NUMERO ENTERO VALIDO"+reset_color)
            #
        #        

        for factura in facturas:
            if factura["factura"] == factura_id:
                # Eliminar la factura encontrada
                facturas.remove(factura)
                #print(factura)
                print(purple_color+"Factura eliminada exitosamente."+reset_color)
                # Reorganizar los IDs de las facturas restantes
                for idx, factura in enumerate(facturas, start=1):
                    print(idx)
                    factura["factura"] = idx
                    json_file.save(facturas)
                return
        # Si no se encuentra la factura
        print(red_color+"NO SE ENCONTRO NIGUNA FACTURA CON EL ID PROPROCIONADO."+reset_color)
        #print(facturas)
    #
    
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Venta"+" "*35+"██")
        gotoxy(2,4);invoice= input("Ingrese Factura: ")
        if invoice.isdigit():
            invoice = int(invoice)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.find("factura",invoice)
            print(f"Impresion de la Factura#{invoice}")
            print(invoices)
        else:    
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            print("Consulta de Facturas")
            for fac in invoices:
                print(f"{fac['factura']}   {fac['Fecha']}   {fac['cliente']}   {fac['total']}")
            
            # suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), 
            # invoices,0)
            # totales_map = list(map(lambda invoice: invoice["total"], invoices))
            # total_client = list(filter(lambda invoice: invoice["cliente"] == "Dayanna Vera", invoices))

            # max_invoice = max(totales_map)
            # min_invoice = min(totales_map)
            # tot_invoices = sum(totales_map)
            # print("filter cliente: ",total_client)
            # print(f"map Facturas:{totales_map}")
            # print(f"              max Factura:{max_invoice}")
            # print(f"              min Factura:{min_invoice}")
            # print(f"              sum Factura:{tot_invoices}")
            # print(f"              reduce Facturas:{suma}")
        x=input("presione una tecla para continuar...")    

#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu("Menu Facturacion",["1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()    
            menu_clients = Menu("Menu Clientes",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            Client = CrudClients()

            if opc1 == "1":
                borrarPantalla()
                Client.create()
            elif opc1 == "2":
                borrarPantalla()
                Client.update()
            elif opc1 == "3":
                borrarPantalla()
                Client.delete()
            elif opc1 == "4":
                borrarPantalla()
                Client.consult()
                time.sleep(2)            

            print("Regresando al menu Clientes...")
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()    
            menu_products = Menu("Menu Productos",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc2 = menu_products.menu()
            product = CrudProducts()
            if opc2 == "1":
                borrarPantalla()
                product.create()
            elif opc2 == "2":
                borrarPantalla()
                product.update()
            elif opc2 == "3":
                borrarPantalla()
                product.delete()
            elif opc2 == "4":
                borrarPantalla()
                product.consult()
    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu("Menu Ventas",["1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()  
            elif opc3 == "2":
                sales.consult()
                time.sleep(2)
            elif opc3 == "3":
                borrarPantalla()
                sales.update()
            elif opc3 == "4":
                borrarPantalla()
                sales.delete()
    print("Regresando al menu Principal...")
    # time.sleep(2)            

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()

