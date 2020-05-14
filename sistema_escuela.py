import sys
import sqlite3
from sqlite3 import Error
import pandas as pd

# Creación de la base de datos en SQLite3
try:
    with sqlite3.connect("Escuela.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Alumno (Matricula INTEGER PRIMARY KEY, Nombre TEXT NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS Asignatura (ID_Asignatura INTEGER PRIMARY KEY, Materia TEXT NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS Calificaciones (Matricula INTEGER, ID_Asignatura INTEGER, Calificacion INTEGER, FOREIGN KEY (Matricula) REFERENCES Alumno(Matricula), FOREIGN KEY (ID_Asignatura) REFERENCES Asignatura(ID_Asignatura));")
        print("Tablas creadas exitosamente! \n")
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

# Guardar asignaturas a la base de datos
try:
    with sqlite3.connect("Escuela.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Asignatura VALUES(1, 'Programacion');")
        c.execute("INSERT INTO Asignatura VALUES(2, 'Contabilidad');")
        c.execute("INSERT INTO Asignatura VALUES(3, 'Redes');")
        c.execute("INSERT INTO Asignatura VALUES(4, 'Economia');")
        c.execute("INSERT INTO Asignatura VALUES(5, 'Ingles');")
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

# Funciones de inserción de datos
def guardar_alumnos(matricula, nombre):
    try:
        with sqlite3.connect("Escuela.db") as conn:
            c = conn.cursor()
            valores = {"Matricula":matricula, "Nombre":nombre}
            c.execute("INSERT INTO Alumno VALUES(:Matricula,:Nombre)", valores)
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

def guardar_notas(matricula, clave, cal):
    try:
        with sqlite3.connect("Escuela.db") as conn:
            c = conn.cursor()
            valores = {"Matricula":matricula, "Clave":clave, "Cal":cal}
            c.execute("INSERT INTO Calificaciones VALUES(:Matricula,:Clave,:Cal)", valores)                                                                                                 #a
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

# Inicio del programa

def menu_principal():
    print("\n- MENÚ DEL SISTEMA -")
    print("[1] Agregar alumnos")
    print("[2] Ingresar calificaciones")
    print("[3] Estadisticos descriptivos")
    print("[4] Asignaturas reprobadas")
    print("[5] Reporte de calificaciones")
    print("[6] Exportación")
    print("[7] Consulta SQL con JOINS")
    print("[9] Salir")
    
diccionario_alumnos = {}
diccionario_calificaciones = {}

ciclo = True
while ciclo:
    continuar = True
    menu_principal()
    opcion = int(input("Eliga el número de la opción que desee: "))
    # opcion = int(input("- MENÚ DEL SISTEMA - \n [1] Agregar alumnos \n [2] Ingresar calificaciones \n [3] Estadisticos descriptivos \n [4] Estudiantes Reprobados \n [5] Ver las calificaciones de los alumnos \n [6] Exportación \n \n Eliga el número de la opción que desee: "))
    
    if opcion == 1:
        
        while continuar:
            print("Proporcione los datos de los alumnos, capture la clave 0 (cero) para terminar.")
            
            matricula = int(input("Ingrese la matricula del nuevo estudiante: "))
            
            if matricula == 0:
                continuar = False
            elif matricula not in (diccionario_alumnos.keys()):
                nombre = input("Ingrese el nombre del nuevo estudiante: ")
                guardar_alumnos(matricula, nombre)
                
                diccionario_alumnos[matricula] = [nombre]
                print("\n -- Alumno agregado -- \n")
                print(diccionario_alumnos)
                print("")
            else:
                print("\n Esa matricula YA EXISTE, no se permiten matriculas duplicadas.")
                print("Esta es la lista de alumnos registrados: ")
    
    elif opcion == 2:
        
        while continuar:
            print("Proporcione las calificaciones de cada alumno, capture la clave 0 (cero) para terminar.")
            
            matricula = int(input("Ingresa la matricula del estudiante a calificar: "))
            
            if matricula == 0:
                continuar = False
            elif matricula in (diccionario_alumnos.keys()):
                name = (input("Ingresa el nombre del estudiante a calificar: "))
                
                cal1 = int(input("Ingrese la calificacion de Programacion: "))

                cal2 = int(input("Ingrese la calificacion de Contabilidad: "))

                cal3 = int(input("Ingrese la calificacion de Redes: "))

                cal4 = int(input("Ingrese la calificacion de Economia: "))

                cal5 = int(input("Ingrese la calificacion de Ingles: "))
                if cal1 <= 100 and cal2 <= 100 and cal3 <= 100 \
                   and cal4 <= 100 and cal5 <= 100:
                    guardar_notas(matricula, 1, cal1)
                    guardar_notas(matricula, 2, cal2)
                    guardar_notas(matricula, 3, cal3)
                    guardar_notas(matricula, 4, cal4)
                    guardar_notas(matricula, 5, cal5)
                    
                    diccionario_calificaciones[matricula] = [name, cal1, cal2, cal3, cal4, cal5]
                else:
                    print("\n -- Ingresaste una calificacion invalida -- \n")
            else:
                print("Ese alumno no existe en el registro \n")
            print("\n Lista de alumnos: \n")
            print(diccionario_alumnos)
            print("")
    
    elif opcion == 3:
        
        try:
            notas_alumnos = pd.DataFrame(diccionario_calificaciones)
            notas_alumnos.index = ["Nombre", "Programacion", "Contabilidad", "Redes", "Economia", "Ingles"]
            
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
    
    elif opcion == 7:
        try:
            with sqlite3.connect("Escuela.db") as conn:
                c = conn.cursor()
                c.execute("SELECT Nombre, Materia, Calificacion FROM Calificaciones INNER JOIN Alumno ON Calificaciones.Matricula = Alumno.Matricula INNER JOIN Asignatura ON Calificaciones.ID_Asignatura = Asignatura.ID_Asignatura;")
                registros = c.fetchall()
            
            for registro in registros:
                print(registro)
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
            
    elif opcion == 9:
        ciclo = False
    else:
        print(f"La opción {opcion} no es valida, asegurese de capturar una opción numerica. \n")
        
print("PROGRAMA CONCLUIDO")
        
            
        
        
    
        


