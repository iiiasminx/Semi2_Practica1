#CREACIÓN

DROP_INICIAL=('DROP TABLE if exists temp;')
TEMP_CREATION =('CREATE TABLE temp(artist VARCHAR(50),song VARCHAR(500),duration_ms int,explicit bit,'
    'year int,popularity decimal(10,4),danceability decimal(10,4),energy decimal(10,4),llave int,' 
    'loudness decimal(10,4),mode decimal(10,4),speechiness decimal(10,4),acousticness decimal(10,4),'
    'instrumentalness decimal(10,7),liveness decimal(10,4),valence decimal(10,4),tempo decimal(10,4),'
    'genre varchar(50) );')

ASIGNACION_CREATE = ('CREATE TABLE Asignacion( ID_Asignacion INT NOT NULL IDENTITY(1,1) PRIMARY KEY, Extra VARCHAR(50));')
ASIGNACION_DELETE = ('DROP TABLE if exists Asignacion;')


ARTIST_CREATE = ('CREATE TABLE Artist( ID_Artist INT NOT NULL IDENTITY(1,1) PRIMARY KEY, Name VARCHAR(50));')
ARTIST_DELETE = ('DROP TABLE if exists Artist;')

GENERO_CREATE = ('CREATE TABLE Genero( ID_Genero INT NOT NULL IDENTITY(1,1) PRIMARY KEY, Name VARCHAR(50));')
GENERO_DELETE = ('DROP TABLE if exists Genero;')

SONG_CREATE = ('CREATE TABLE Song(ID_Song INT NOT NULL IDENTITY(1,1) PRIMARY KEY,'
                'Name VARCHAR(500),duration_ms int,explicit bit,'
                'year int);')
SONG_CREATE1 = ('CREATE TABLE Song(ID_Song INT NOT NULL IDENTITY(1,1) PRIMARY KEY,'
                'id_Asignacion int FOREIGN KEY REFERENCES Asignacion(ID_Asignacion) ON DELETE CASCADE ON UPDATE CASCADE,'
                'Name VARCHAR(500),duration_ms int,explicit bit,'
                'year int);')
SONG_DELETE = ('DROP TABLE if exists Song;')

DETALLEA_CREATE = ('CREATE TABLE DetalleAsignacion(ID_Detalle INT NOT NULL IDENTITY(1,1) PRIMARY KEY,'
                    'id_Song int FOREIGN KEY REFERENCES Song(ID_Song) ON DELETE CASCADE ON UPDATE CASCADE,'
                    'id_Genero int FOREIGN KEY REFERENCES Genero(ID_Genero) ON DELETE CASCADE ON UPDATE CASCADE'
                    ');')
DETALLEA_DELETE = ('DROP TABLE if exists DetalleAsignacion;')

HECHOS_CREATE = ('CREATE TABLE Hechos(ID_Hecho INT NOT NULL IDENTITY(1,1) PRIMARY KEY,'
                'id_Artist int FOREIGN KEY REFERENCES Artist(ID_Artist) ON DELETE CASCADE ON UPDATE CASCADE,'
                'id_Song int FOREIGN KEY REFERENCES Song(ID_Song) ON DELETE CASCADE ON UPDATE CASCADE,'
                'popularity decimal(10,4),danceability decimal(10,4),energy decimal(10,4),llave int,' 
                'loudness decimal(10,4),mode decimal(10,4),speechiness decimal(10,4),acousticness decimal(10,4),'
                'instrumentalness decimal(10,7),liveness decimal(10,4),valence decimal(10,4),tempo decimal(10,4),' ');')
HECHOS_DELETE = ('DROP TABLE if exists Hechos;')


