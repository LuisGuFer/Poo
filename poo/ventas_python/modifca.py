from clsJson import JsonFile
from utilities import borrarPantalla, gotoxy, green_color, blue_color, reset_color,red_color,purple_color
import datetime
import os 

import time,sys
path, _ = os.path.split(os.path.abspath(__file__))

class ModificarFactura:
    def __init__(self, path):
        self.path = path
        
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
    def modificar_factura(self):
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
    def eliminar_factura(self) :
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

    # Llamada a la función para eliminar una factura

# Ejemplo de uso
# Ruta al archivo de facturas
modificador = ModificarFactura(path)
# modificador.eliminar_factura()
modificador.modificar_factura()

# modificador.mostrar_facturas()