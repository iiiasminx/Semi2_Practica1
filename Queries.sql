--Consulta 1
select TOP (10)  a.ID_Artist, a.Name as Artista, count(h.id_Artist) as Reproducciones
from Artist a, Hechos h
where h.id_Artist = a.ID_Artist
group by a.Name, a.ID_Artist
order by count(h.id_Artist) desc

-- Consulta 2
select TOP (10) s.ID_Song, s.Name as Cancion, count(h.id_Song) as Reproducciones
from Song s, Hechos h
where h.id_Song = s.ID_Song
group by s.ID_Song, s.Name
order by count(h.id_Song) desc

-- Consulta 3
select TOP (5) g.ID_Genero, g.Name as Genero, count(d.id_Genero) as Reproducciones  
from Genero g, DetalleAsignacion d
where g.ID_Genero = d.id_Genero 
group by g.ID_Genero, g.Name
order by count(d.id_Genero) desc

-- Consulta 3.5
select g.ID_Genero, g.Name as Genero, count(h.ID_Artist) as Reproducciones
from Artist a, Genero g, DetalleAsignacion d, Song s, Hechos h
where g.ID_Genero = d.id_Genero
and d.id_Song = s.ID_Song
and s.ID_Song = h.id_Song
and h.id_Artist = a.ID_Artist
group by g.ID_Genero, g.Name
order by count(h.id_Song) desc

-- Consulta 4
select g.ID_Genero, g.Name as Genero, a.Name as Artista, count(h.id_Song) as Reproducciones
from Artist a, Genero g, DetalleAsignacion d, Song s, Hechos h
where g.ID_Genero = d.id_Genero
and d.id_Song = s.ID_Song
and s.ID_Song = h.id_Song
and h.id_Artist = a.ID_Artist
group by g.ID_Genero, g.Name, a.Name
order by count(h.id_Song) desc


-- Consulta 7 
select a.ID_Artist, a.Name as Artista, AVG(h.popularity) as Popularidad
from Artist a, Hechos h
where a.ID_Artist = h.id_Artist
group by a.ID_Artist, a.Name
order by AVG(h.popularity) desc

-- Consulta 8
select s.ID_Song, s.Name as Cancion, AVG(h.popularity) as Popularidad from Song s, Hechos h where s.ID_Song = h.id_Song group by s.ID_Song, s.Name order by AVG(h.popularity) desc



-- Consulta 9
select g.ID_Genero, g.Name, AVG(h.popularity) as Popularidad from Genero g, Hechos h, DetalleAsignacion d, Song s where g.ID_Genero = d.id_Genero and d.id_Song = s.ID_Song and s.ID_Song = h.id_Song group by g.ID_Genero, g.Name order by AVG(h.popularity) desc




