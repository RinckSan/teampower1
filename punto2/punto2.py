worker = {}

Trabajador = lambda nombre, edad, ocupacion: print(worker)

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ocupacion = input("Ingrese su ocupacion: ")

worker['nombre'] = nombre
worker['edad'] = edad
worker['ocupacion'] = ocupacion 

persona = Trabajador(worker)
print (persona)


