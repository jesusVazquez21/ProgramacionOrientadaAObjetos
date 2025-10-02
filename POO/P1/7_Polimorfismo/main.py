from Coches import *
import os
#Solicitar los datos que posteriormente seran los atributs del objeto


def autos():
    # num_coches = int(input("Cuantos coches tiene?"))
    # for i in range(0,num_coches):
    print("Datos del auto")
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    coche1 = Coches(marca,color,modelo,velocidad,potencia,plazas)
        
    coche1=Coches(marca, color, modelo, velocidad, potencia, plazas)
        
    print(f"Datos del Vehiculo: \n Marca:{coche1.marca()} \n color: {coche1.color()} \n Modelo: {coche1.modelo()} \n velocidad: {coche1.velocidad()} \n caballaje: {coche1.caballaje()} \n plazas: {coche1.plazas()} ")

def camionetas():
    print("Datos del vehiculo")
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    traccion=input("Ingresar el tipo de traccion: ").upper()
    cerrada=input("Ingresar SI/NO si es cerrada o no: ").upper()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False


    coche1=Camionetas(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada)

    print(f"Datos del Vehiculo: \n Marca:{coche1.marca()} \n color: {coche1.color()} \n Modelo: {coche1.modelo()} \n velocidad: {coche1.velocidad()} \n caballaje: {coche1.caballaje()} \n plazas: {coche1.plazas()} \n traccion: {coche1.traccion()} \n cerrada: {coche1.cerrada()} ")

def camiones():
    print("Datos del camion")
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    eje=int(input("Ingresar la capacidad de carga: "))
    capacidadCarga=int(input("Ingresar la capacidad de carga: "))


    coche1=Camionetas(marca, color, modelo, velocidad, potencia, plazas, eje, capacidadCarga)

    print(f"Datos del Vehiculo: \n Marca:{coche1.marca()} \n color: {coche1.color()} \n Modelo: {coche1.modelo()} \n velocidad: {coche1.velocidad()} \n caballaje: {coche1.caballaje()} \n plazas: {coche1.plazas()} \n traccion: {coche1.eje()} \n cerrada: {coche1.capacidadCarga()} ")



opcion=1
while opcion!=4:
    os.system("cls")
    print("..:: MENU PRINCIPAL ::..")
    opcion=input("\n\t 1.- Autos \n\t 2.- Camionetas\n\t 3.- Camiones\n\t 4.- Salir\n\t Elige una opción: ").lower().strip()
    match opcion: 
        case "1": 
            autos()
            input("Oprima tecla para continuar")
        case "2":
            camionetas()
            input("Oprima tecla para continuar")
        case "3":
            camiones()
            input("Oprima tecla para continuar")
        case "4":
            print("Salir")
            input("Oprima tecla para continuar")
        case _:
            print("Opción Invalida..... Vuelva a intentarlo")
            input("Oprima tecla para continuar")  








''' 
num_coches = int(input("Cuantos coches tiene?"))
for i in range(0,num_coches):
    print("Datos del auto")
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    coche = Coches(marca,color,modelo,velocidad,potencia,plazas)

'''