--Consulta 1
select TOP (10)  a.ID_Artist, a.Name as Artista, count(h.id_Artist) as Reproducciones
from Semi2_P1.dbo.Artist a, Semi2_P1.dbo.Hechos h
where h.id_Artist = a.ID_Artist
group by a.Name, a.ID_Artist
order by count(h.id_Artist) desc

-- Consulta 2
select TOP (10) s.ID_Song, s.Name as Cancion, count(h.id_Song) as Reproducciones
from Semi2_P1.dbo.Song s, Semi2_P1.dbo.Hechos h
where h.id_Song = s.ID_Song
group by s.ID_Song, s.Name
order by count(h.id_Song) desc

-- Consulta 3
select TOP (5) g.ID_Genero, g.Name as Genero, count(d.id_Genero) as Reproducciones  
from Semi2_P1.dbo.Genero g, Semi2_P1.dbo.DetalleAsignacion d
where g.ID_Genero = d.id_Genero 
group by g.ID_Genero, g.Name
order by count(d.id_Genero) desc

-- Consulta 3.5
select g.ID_Genero, g.Name as Genero, count(h.ID_Artist) as Reproducciones
from Semi2_P1.dbo.Artist a, Semi2_P1.dbo.Genero g, Semi2_P1.dbo.DetalleAsignacion d, Semi2_P1.dbo.Song s, Semi2_P1.dbo.Hechos h
where g.ID_Genero = d.id_Genero
and d.id_Song = s.ID_Song
and s.ID_Song = h.id_Song
and h.id_Artist = a.ID_Artist
group by g.ID_Genero, g.Name
order by count(h.id_Song) desc

-- Consulta 4
-- El artista más reproducido de cada género 


Select g.Name, a.Name as Artista, count(a.Name) as Reproducciones
from Artist a, Hechos h, Song s, DetalleAsignacion d, Genero g
where a.ID_Artist = h.id_Artist
and h.id_Song = s.ID_Song
and s.ID_Song = d.id_Song
and d.id_Genero = g.ID_Genero
and a.Name in
(
select top (1) r.Name
from Artist r, Hechos e, Song o, DetalleAsignacion t, Genero n
where r.ID_Artist = e.id_Artist
and e.id_Song = o.ID_Song
and o.ID_Song = t.id_Song
and t.id_Genero = n.ID_Genero
and n.ID_Genero = g.ID_Genero
group by r.Name
order by count(r.Name) desc
)
group by g.Name, g.ID_Genero, a.Name
order by count(a.Name) desc


-- Consulta 5
-- La canción más reproducida por cada género

Select g.Name, s.Name as Cancion, count(s.Name) as Reproducciones
from Hechos h, Song s, DetalleAsignacion d, Genero g
where h.id_Song = s.ID_Song
and s.ID_Song = d.id_Song
and d.id_Genero = g.ID_Genero
and s.Name in (
select top (1) o.Name
from Song o, Hechos e, DetalleAsignacion t, Genero n
where e.id_Song = o.ID_Song
and o.ID_Song = t.id_Song
and t.id_Genero = n.ID_Genero
and n.ID_Genero = g.ID_Genero
group by o.Name
order by count(o.Name) desc
)
group by g.Name, s.Name
order by count(s.Name) desc


-- Consulta 6
-- La canción más reproducida por año de lanzamiento 

select s.year,  s.Name as Cancion, count(h.id_Song) as Reproducciones 
from Hechos h, Song s
where s.ID_Song = h.id_Song
and s.ID_Song in 
(
select top (1) o.ID_Song
from Hechos e, Song o
where o.ID_Song = e.id_Song
and o.year = s.year
group by o.ID_Song
order by count(o.ID_Song) desc
)
group by h.id_Artist, h.id_Song, s.Name, s.year
order by count(h.id_Song) desc


-- Consulta 7 
select a.ID_Artist, a.Name as Artista, AVG(h.popularity) as Popularidad
from Semi2_P1.dbo.Artist a, Semi2_P1.dbo.Hechos h
where a.ID_Artist = h.id_Artist
group by a.ID_Artist, a.Name
order by AVG(h.popularity) desc



-- Consulta 8
select s.ID_Song, s.Name as Cancion, AVG(h.popularity) as Popularidad 
from Semi2_P1.dbo.Song s, Semi2_P1.dbo.Hechos h 
where s.ID_Song = h.id_Song 
group by s.ID_Song, s.Name 
order by AVG(h.popularity) desc



-- Consulta 9
select g.ID_Genero, g.Name, AVG(h.popularity) as Popularidad 
from Semi2_P1.dbo.Genero g, Semi2_P1.dbo.Hechos h, Semi2_P1.dbo.DetalleAsignacion d, Semi2_P1.dbo.Song s 
where g.ID_Genero = d.id_Genero and d.id_Song = s.ID_Song and s.ID_Song = h.id_Song 
group by g.ID_Genero, g.Name 
order by AVG(h.popularity) desc




