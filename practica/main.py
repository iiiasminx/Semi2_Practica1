#librerías

from ast import If
import pyodbc
import pandas as pd
import config
import logging
from queries import *
import logging

def crearModelo():
    print("Creando Modelo")

    cursor = conn.cursor()
    cursor.execute(DROP_INICIAL)
    
    cursor.execute(HECHOS_DELETE)
    cursor.execute(DETALLEA_DELETE)
    cursor.execute(SONG_DELETE)
    cursor.execute(ARTIST_DELETE)
    cursor.execute(GENERO_DELETE)
    cursor.execute(ASIGNACION_DELETE)   

    logger.info('Tablas eliminiadas con éxito :D')
    

    cursor.execute(TEMP_CREATION)
    cursor.execute(ARTIST_CREATE)
    cursor.execute(GENERO_CREATE)
    cursor.execute(ASIGNACION_CREATE)

    cursor.execute(SONG_CREATE)    
    cursor.execute(DETALLEA_CREATE)    
    cursor.execute(HECHOS_CREATE)    
    print("Creación de modelo finalizada")
    

    
def cargar_temporal(df):
    cursor = conn.cursor()
    i = 0
    for row in df.itertuples():
        if(i==0):
            i = i +1
            continue
        artist = str(row[1].replace("'","''"))
        song = str(row[2].replace("'","''"))
        genre = str(row[18].replace("'","''"))
        
        #temp
        query = (f'INSERT INTO temp VALUES(\'{artist}\',\'{song}\',{row[3]},\'{row[4]}\',{row[5]},{row[6]},{row[7]},{row[8]},{row[9]},{row[10]},{row[11]},{row[12]},{row[13]},{row[14]},{row[15]},{row[16]},{row[17]},\'{genre}\')')
        #logger.info(query)
        cursor.execute(query)

        #Artist
        query2 = (f'INSERT INTO Artist (Name) SELECT \'{artist}\' WHERE NOT EXISTS  (SELECT Name FROM Artist WHERE Name = \'{artist}\')')        
        #logger.info(query2)
        cursor.execute(query2)

        generos = genre.split(", ")

        #Generos
        for x in generos:
            query3 = (f'INSERT INTO Genero (Name) SELECT \'{x}\' WHERE NOT EXISTS  (SELECT Name FROM Genero WHERE Name = \'{x}\')')        
            #logger.info(query3)
            cursor.execute(query3)

        bit = 1 if row[4] else 0

        # Songs
        query4 = (f'INSERT INTO Song (Name, duration_ms, explicit, year ) SELECT \'{song}\',{row[3]},\'{bit}\',{row[5]} WHERE NOT EXISTS  (SELECT Name, duration_ms, explicit, year FROM Song WHERE Name = \'{song}\' AND duration_ms={row[3]} AND explicit = {bit} AND year= {row[5]} )')     
        #logger.info(query4)
        cursor.execute(query4)

        # Detalle Asignación
        getidSong = (f'SELECT * FROM Song WHERE Name = \'{song}\' AND duration_ms={row[3]} AND explicit = {bit} AND year= {row[5]}')
        row1  = cursor.execute(getidSong).fetchone()
        idSong = row1.ID_Song

        for x in generos:
            getidGenre = (f'SELECT * FROM Genero WHERE Name = \'{x}\'')        
            row2  = cursor.execute(getidGenre).fetchone()
            idGenre = row2.ID_Genero

            query5 = (f'INSERT INTO DetalleAsignacion (id_Song, id_Genero) SELECT {idSong}, {idGenre} WHERE NOT EXISTS  (SELECT id_Song, id_Genero FROM DetalleAsignacion WHERE id_Song= {idSong} AND id_Genero= {idGenre})')        
            #logger.info(query5)
            cursor.execute(query5)

        # Hecho
        getidArtist = (f'SELECT * FROM Artist WHERE Name = \'{artist}\'')
        row3  = cursor.execute(getidArtist).fetchone()
        idArtist = row3.ID_Artist

        query6 = (f'INSERT INTO Hechos (id_Artist, id_Song, popularity, danceability, energy, llave, loudness, mode,speechiness, acousticness, instrumentalness, liveness, valence, tempo ) VALUES ({idArtist},{idSong},{row[6]},{row[7]},{row[8]},{row[9]},{row[10]},{row[11]},{row[12]},{row[13]},{row[14]},{row[15]},{row[16]},{row[17]}) ')
        #logger.info(query6)
        cursor.execute(query6)        

    logger.info("C'est finit :3")

def cargarInfo(): 
    print("Cargando Información")
    print("Por favor ingresa la ruta del archivo")
    ruta = input()

    try:
        data = pd.read_csv(ruta)
        df = pd.DataFrame(data)
        logger.info("Dataset leido exitosamente! :D")
        cargar_temporal(df)
    except Exception as e:
        logger.error(e)
        print("Algo salió mal, muerte :c")
        conn.close()
        exit()
    
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
    cursor = conn.cursor()

    if consulta == "1":
        logger.info("consulta 1")

        consulta1 = (f'select TOP (10)  a.ID_Artist, a.Name as Artista, count(h.id_Artist) as Reproducciones from Artist a, Hechos h where h.id_Artist = a.ID_Artist group by a.Name, a.ID_Artist order by count(h.id_Artist) desc')
        rows = cursor.execute(consulta1).fetchall()

        print("1. Top 10 artistas con más reproducciones -------------------------")
        print("ID   |   Artista   |   Reproducciones")
        for row in rows:
            print(row.ID_Artist, "| ", row.Artista, "| ", row.Reproducciones)

    elif consulta == "2":
        logger.info("consulta 2")

        consulta2 = (f'select TOP (10) s.ID_Song, s.Name as Cancion, count(h.id_Song) as Reproducciones from Song s, Hechos h where h.id_Song = s.ID_Song group by s.ID_Song, s.Name order by count(h.id_Song) desc')
        rows = cursor.execute(consulta2).fetchall()

        print("2. Top 10 canciones más reproducidas ------------------------------")
        print("ID   |   Cancion   |   Reproducciones")
        for row in rows:
            print(row.ID_Song, "| ", row.Cancion, "| ", row.Reproducciones)

    elif consulta == "3":
        logger.info("consulta 3") 

        consulta3 = (f'select TOP (5) g.ID_Genero, g.Name as Genero, count(d.id_Genero) as Reproducciones from Genero g, DetalleAsignacion d where g.ID_Genero = d.id_Genero  group by g.ID_Genero, g.Name order by count(d.id_Genero) desc ')
        rows = cursor.execute(consulta3).fetchall()

        print("3. Top 5 géneros más reproducidos -----------------------------------")
        print("ID   |   Genero   |   Reproducciones")
        for row in rows:
            print(row.ID_Genero, "| ", row.Genero, "| ", row.Reproducciones)

    elif consulta == "4":
        logger.info("consulta 4") 
    elif consulta == "5":
        logger.info("consulta 5") 
    elif consulta == "6":
        logger.info("consulta 6") 
    elif consulta == "7":
        logger.info("consulta 7") 

        consulta7 = (f'select TOP (10) a.ID_Artist, a.Name as Artista, AVG(h.popularity) as Popularidad from Artist a, Hechos h where a.ID_Artist = h.id_Artist group by a.ID_Artist, a.Name order by AVG(h.popularity) desc')
        rows = cursor.execute(consulta7).fetchall()

        print("7. Top 10 artistas más populares -----------------------------------")
        print("ID   |   Artista   |   Popularidad")
        for row in rows:
            print(row.ID_Artist, "| ", row.Artista, "| ", row.Popularidad)

    elif consulta == "8":
        logger.info("consulta 8") 

        consulta8 = (f'select TOP (10) s.ID_Song, s.Name as Cancion, AVG(h.popularity) as Popularidad from Song s, Hechos h where s.ID_Song = h.id_Song group by s.ID_Song, s.Name order by AVG(h.popularity) desc')
        rows = cursor.execute(consulta8).fetchall()

        print("8. Top 10 canciones más populares -----------------------------------")
        print("ID   |   Cancion   |   Popularidad")
        for row in rows:
            print(row.ID_Song, "| ", row.Cancion, "| ", row.Popularidad)

    elif consulta == "9":
        logger.info("consulta 9") 

        consulta9 = (f'select TOP (5) g.ID_Genero, g.Name as Genero, AVG(h.popularity) as Popularidad from Genero g, Hechos h, DetalleAsignacion d, Song s where g.ID_Genero = d.id_Genero and d.id_Song = s.ID_Song and s.ID_Song = h.id_Song group by g.ID_Genero, g.Name order by AVG(h.popularity) desc')
        rows = cursor.execute(consulta9).fetchall()

        print("9. Top 5 géneros más populares -----------------------------------")
        print("ID   |   Genero   |   Popularidad")
        for row in rows:
            print(row.ID_Genero, "| ", row.Genero, "| ", row.Popularidad)

    elif consulta == "10":
        logger.info("consulta 10") 
        



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
        conn.close()
        print("Conexión finalizada correctamente. Bai O/")
        return   
    
    inicial()



#INICIO DE LA EJECUCIÓN

#LOGS 

logger = logging.getLogger('Semi_2_Ejemplo')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler('logs.log')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


#CONEXIÓN       

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=GTTI-108692;"
    "Database=Semi2_P1;"
    "Trusted_Connection=yes;"
,autocommit=True)
logger.info("Conexion realizada con exito")
inicial()