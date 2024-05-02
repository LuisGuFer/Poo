# # Crear un diccionario vacío
# mi_diccionario = {}

# # Definir la estructura
# estructura = {"Nombre": "", "Edad": "", "Colegio": ""}

# # Solicitar al usuario que ingrese los datos hasta que decida detenerse
# while True:
#     # Crear una copia de la estructura para evitar sobrescribir los datos ingresados previamente
#     nueva_estructura = estructura.copy()
    
#     # Solicitar al usuario que ingrese los datos
#     nueva_estructura["Nombre"] = input("Ingresa tu nombre: ")
#     nueva_estructura["Edad"] = input("Ingresa tu edad: ")
#     nueva_estructura["Colegio"] = input("Ingresa el nombre de tu colegio: ")
    
#     # Agregar la nueva estructura al diccionario
#     mi_diccionario[len(mi_diccionario) + 1] = nueva_estructura
    
#     # Preguntar al usuario si desea agregar más datos
#     continuar = input("¿Deseas agregar más datos? (s/n): ")
#     if continuar.lower() != 's':
#         break

# # Mostrar el diccionario resultante
# for i,y in mi_diccionario.items():
#     print(i)
# print(mi_diccionario)



import random
# class mm:
#     def genera_id(self):
#         id_persona = ''.join([str(random.randint(0, 9)) for _ in range(10)])
#         print("ID de la persona:", id_persona)


# Decorador para validar si la cédula pertenece a Ecuador

# Clase para generar números de identificación
class GeneradorID:
    def validar_cedula(func):
        def wrapper(*args, **kwargs):
            
            id_persona = func(*args, **kwargs)
            codigo_provincia = id_persona[:2]
            while codigo_provincia not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]:
                id_persona = func(*args,**kwargs)
                codigo_provincia = id_persona[:2]
            return id_persona
        return wrapper

    @validar_cedula
    def generar_id(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])
        

# Uso del decorador para generar y validar una cédula
id_persona = GeneradorID()
print(id_persona.generar_id())


