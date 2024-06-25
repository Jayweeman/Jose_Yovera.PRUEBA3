import os
os.system('cls')
import random


print(" BIENVENIDO A 'AUTO SEGURO' ")
print()



pregunta = 's'
while True:
     
    try:
        
        opcion = int(input("Seleccione opcion: "))
        
    except:
        
        opcion = 0
    
    datos_vehiculo = [
        {'Tipo': tipo, 'Patente': patente, 'Marca': marca, 'Precio': precio,
        'multas': multas, 'Fecha de registro vehiculo': fecha_registro_vehiculo, 'Run': run,
        'Nombre y apellido': nombre_apellido}
        ]    
    if opcion == 1:
        print("Grabar - almacenando datos de vehiculo")
        print()
        tipo = ('')
        tipo = input("Ingrese tipo de vehiculo: ")
        patente = 0
        patente = int(input(f"Ingrese patente de vehiculo: "))
        marca = 0
        marca = input("Marca de vehiculo: ")
        precio = 0
        precio = int(input(f"Ingrese precio de vehiculo:"))
        multas = 0
        multas = int(input(f"En caso de infracciones, indique multa de vehiculo: "))
        fecha_registro_vehiculo = 0
        fecha_registro_vehiculo = int(input(f"fecha de registro del vechiculo: "))
        run = 0
        run = int(input("Ingrese run sin digito verificador: "))
        nombre_apellido = ('')
        nombre_apellido = input("Ingrese nombre y apellido del propietario: ")
    
                    
    elif opcion == 2:
        
    
        print("Buscar - Mostrando información:  ")
        
    
    
    elif opcion == 3:
    
        print("Imprimiendo certificados")
        print("""
        
        1.Emision de contaminantes
        2.Anotaciones vigentes
        3.Multas"
              """)
        try:
            opcion = int(input("Seleccione una opcion:"))
        except:
            opcion = 0
            
        if opcion == 1:
            print("Imprimiendo certificado de emision de contaminantes...")
        elif opcion == 2:
            print("Imprimiendo certificado de anotaciones vigentes...")
        elif opcion == 3:
            print("Imprimiendo certificado de Multas")
        else:
            opcion = 0
            print("opcion invalida")
        
        
    else: 
        opcion == 4
        print("Saliendo del programa. bye")
            
salir = input("Desea salir del programa?: s/n", pregunta)



