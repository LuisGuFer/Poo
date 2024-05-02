import os
import json
path, _ = os.path.split(os.path.abspath(__file__))
path = path+'/archivos/products.json'
with open(path,"r") as file:
    data = json.load(file)
while True:
    nombre=input("Ingrese nombre ")
    function  = lambda name : any (nombre.lower() == lis["descripcion"].lower() for lis in data)
    result = function(data)
    if result:
        break
    else:
        print("¡NOMBRE NO ENCONTRADO EN LA LISTA DE PRDOUCTOS!")
    #
#        
print(result)
