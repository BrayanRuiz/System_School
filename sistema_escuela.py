import pandas as pd

diccionario_alumnos = {}
diccionario_calificaciones = {}

i = 1
while i > 0:
    opcion = int(input("- MENÚ DEL SISTEMA - \n [1] Agregar alumnos \n [2] Ingresar calificaciones \n [3] Estadisticos descriptivos \n [4] Estudiantes Reprobados \n [5] Ver las calificaciones de los alumnos \n [6] Exportación \n \n Eliga el número de la opción que desee: "))
    
    if opcion == 1: 
        
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
            
            eleccion = int(input("\n 1)- Asignaturas \n 2)- Alumnos \n Eliga una opción: "))
            
            if eleccion == 1:
                numbers = notas_alumnos[1:6]
                print(f"Materia:  Calificaciones registradas \n {numbers.T.count()}")
                print(f"Materia:  Promedio General \n {numbers.T.mean()}")
                print(f"Materia:  Desviación estandar \n {numbers.T.std()}")
                print(f"Materia:  Calificación mas baja \n {numbers.T.min()}")
                print(f"Materia:  Calificacion mas alta \n {numbers.T.max()}")
                
                file = open("Estadistica_Asignaturas.txt", "w")
                file.write("%s" %numbers.T.count()+"\n")
                file.write("%s" %numbers.T.mean()+"\n")
                file.write("%s" %numbers.T.std()+"\n")
                file.write("%s" %numbers.T.min()+"\n")
                file.write("%s" %numbers.T.max())
                file.close()
            else:
                numbers = notas_alumnos[1:6]
                print(f"Matricula:  Materias del estudiante \n {numbers.count()}")
                print(f"Matricula:  Promedio General \n {numbers.mean()}")
                print(f"Matricula:  Desviación estandar \n {numbers.std()}")
                print(f"Matricula:  Calificación mas baja \n {numbers.min()}")
                print(f"Matricula:  Calificación mas alta \n {numbers.max()}")
                
                archivo = open("Estadistica_Alumnos.txt", "w")
                archivo.write("%s" %numbers.count()+"\n")
                archivo.write("%s" %numbers.mean()+"\n")
                archivo.write("%s" %numbers.std()+"\n")
                archivo.write("%s" %numbers.min()+"\n")
                archivo.write("%s" %numbers.max())
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
            
    elif opcion == 6:
        
        notas_alumnos = pd.DataFrame(diccionario_calificaciones)
        notas_alumnos.index = ["Nombre", "Programacion", "Contabilidad", "Base de Datos", "Economia", "Ingles"]
        
        elegir = int(input("\n 1)- Exportar a CSV \n 2)- Exportar a JSON \n Eliga una opción: "))
        
        if elegir == 1:
            print("\n Procederemos a crear el archivo CSV....")
            notas_alumnos.to_csv(r'notas_alumnos.csv', index=True, header=True)
            print("-- Exportado -- \n")
        else:
            print("\n Procederemos a crear el archivo JSON....")
            notas_alumnos.T.to_json('notas_alumnos.json', orient= "table")
            print("-- Exportado -- \n")
            
            
        
        
    
        

