USE [Semi2_P1]
GO

INSERT INTO [dbo].[Hechos]
           ([id_Artist]
           ,[id_Song]
           ,[popularity]
           ,[danceability]
           ,[energy]
           ,[llave]
           ,[loudness]
           ,[mode]
           ,[speechiness]
           ,[acousticness]
           ,[instrumentalness]
           ,[liveness]
           ,[valence]
           ,[tempo])
     VALUES (1,1,79,0.434,0.8970,0,-4.9180,1,0.0488,0.0103,0,0.6120,0.6840,148.7260)
GO


select  h.id_Artist, s.Name, s.explicit, count(h.id_Song) as Reproducciones 
from Hechos h, Song s
where s.ID_Song = h.id_Song
and s.explicit = 1
group by h.id_Artist, h.id_Song, s.Name, s.explicit
order by count(h.id_Song) desc

select * from Song

