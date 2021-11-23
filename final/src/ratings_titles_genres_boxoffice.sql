SELECT *
INTO Test.dbo.ratings_titles_genres_boxoffice
FROM (
	SELECT CONVERT(ntext, t1.tconst) as imdb_id, t1.averageRating as imdb_rating, CONVERT(ntext, t1.primaryTitle) as title, t1.startYear as year, CONVERT(ntext, t1.genres) as genres, t2.column3 as boxOffice, t2.column4 as numTickets
	FROM Test.dbo.ratings_titles_genres t1, Test.dbo.titles_boxoffice t2
	WHERE t1.primaryTitle = t2.column2
	AND CONVERT(nvarchar(max), t1.startYear) = CONVERT(nvarchar(max), t2.column1)
	) t3
;
