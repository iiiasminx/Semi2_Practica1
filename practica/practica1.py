import os
def crearModelo():
    print("Creando Modelo")

def cargarInfo(): 
    print("Cargando Información")
    
def consultar(): 
    print("-- Consultas --")
    print("1. Top 10 artistas con más reproducciones")
    print("2. Top 10 canciones más reproducidas")
    print("3. Top 5 géneros más reproducidos")
    print("4. El artista más reproducido de cada género")
    print("5. La canción más reproducida por cada género")
    print("6. La canción más reproducida por año de lanzamiento")
    print("7. Top 10 artistas más populares")
    print("8. Top 10 canciones más populares")
    print("9. Top 5 géneros más populares")
    print("10. La canción explícita más reproducida por género")

    consulta = input()
    print(consulta)

def inicial():
    print("\n\n\n")
    print("UNIVERSIDAD DE SAN CARLOS DE GUATEMALA")
    print("FACULTAD DE INGENIERÍA")
    print("YÁSMIN ELISA MONTERROSO ESCOBEDO")
    print("\n\n-- MENU --\n\n")
    print("1. Crear Modelo")
    print("2. Cargar Información")
    print("3. Realizar Consultas")
    print("4.salir")

    choice = input()
    if choice == "1":
        crearModelo()
    elif choice == "2": 
        cargarInfo()
    elif choice == "3": 
        consultar()
    else:
        print("bai O/")
        return   
    
    inicial()


#INICIO DE TODO    
##inicial()