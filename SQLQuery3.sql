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
     VALUES (1,1,1,1,1,1,1,1,1,1,1,1,1,1)
GO


select * from Hechos

