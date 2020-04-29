import json
import pandas as pd
import os.path

diccionario_alumnos = {}
diccionario_calificaciones = {}

i = 1
while i > 0:
    opcion = int(input("- MENÚ DEL SISTEMA - \n [1] Agregar alumnos \n [2] Ingresar calificaciones \n [3] Estadisticos descriptivos \n [4] Estudiantes Reprobados \n [5] Ver las calificaciones de los alumnos \n \n Eliga el número de la opción que desee: "))
    
    if opcion == 1: #Checar si se queda asi o que se ingresen los 30 alumnos de una
        
        clave = int(input("Ingrese la matricula del nuevo estudiante: "))
        nombre = input("Ingrese el nombre del nuevo estudiante: ")
        
        if clave not in (diccionario_alumnos.keys()):
            diccionario_alumnos[clave] = [nombre]
            print("\n -- Alumno agregado -- \n")
        else:
            print("\n Esa matricula YA EXISTE, no se permiten matriculas duplicadas.")
            print("Esta es la lista de alumnos registrados:")
            
        print(diccionario_alumnos)
        print("\n")
    
    elif opcion == 2:
        
        matricula = int(input("Ingresa la matricula del estudiante a calificar: "))
        name = (input("Ingresa el nombre del estudiante a calificar: "))
        
        if matricula in (diccionario_alumnos.keys()):
            cal1 = int(input("Ingrese la calificacion de Programacion: "))

            cal2 = int(input("Ingrese la calificacion de Contabilidad: "))

            cal3 = int(input("Ingrese la calificacion de Base de Datos: "))

            cal4 = int(input("Ingrese la calificacion de Economia: "))

            cal5 = int(input("Ingrese la calificacion de Ingles: "))
            if cal1 <= 100 and cal2 <= 100 and cal3 <= 100 \
               and cal4 <= 100 and cal5 <= 100:
                diccionario_calificaciones[matricula] = [[name], cal1, cal2, cal3, cal4, cal5]
            else:
                print("Ingresaste una calificacion invalida")
        else:
            print("Ese alumno no existe en el registro \n")
        print("Lista de alumnos: \n")
        print(diccionario_alumnos)
        print()
    
    elif opcion == 3:
        
        try:
            notas_alumnos = pd.DataFrame(diccionario_calificaciones)
            notas_alumnos.index = ["Nombre", "Programacion", "Contabilidad", "Base de Datos", "Economia", "Ingles"]
            
            eleccion = int(input("Eliga una opción: \n 1)- Promedio asignaturas \n 2)- Promedio de alumnos \n"))
            
            if eleccion == 1:
                print("Promedio general de las asignaturas: \n")
                print(notas_alumnos.T.mean(axis = 0))
                print("\n")
                
                file = open("Promedio_Asignaturas.txt", "w")
                file.write("%s" %notas_alumnos.T.mean(axis = 0))
                file.close()
            else:
                print("Promedio de cada alumno registrado: \n")
                print(notas_alumnos[1:6].mean())
                print("\n")
                
                archivo = open("Promedio_Alumnos.txt", "w")
                archivo.write("%s" %notas_alumnos[1:6].mean())
                archivo.close()
        except:
            print("No hay datos en esta seccion para mostrar \n")
    
    elif opcion == 4:
        
        try:
            notas_alumnos = pd.DataFrame(diccionario_calificaciones)
            notas_alumnos.index = ["Nombre", "Programacion", "Contabilidad", "Base de Datos", "Economia", "Ingles"]
                
            print("Aqui se muestran SOLAMENTE las calificaciones reprobadas de cada alumno: \n")
                
            reprobada = notas_alumnos[notas_alumnos[1:6] < 70]
                
            print(reprobada.T)
        except:
            print("No hay datos en esta seccion para mostrar \n")
        
    elif opcion == 5:
        
        try:
            notas_alumnos = pd.DataFrame(diccionario_calificaciones)
            notas_alumnos.index = ["Nombre", "Programacion", "Contabilidad", "Base de Datos", "Economia", "Ingles"]
                
            print("Lista de calificaciones \n")
                
            print(notas_alumnos.T)
            print("\n")
        except:
            print("No hay datos en esta seccion para mostrar \n")
            
        
        
    
        

