SELECT *
INTO Test.dbo.ratings_titles_genres_boxoffice_metacritic
FROM (
	SELECT t1.imdb_id, t1.imdb_rating, t2.metacritic_score, t1.title, t1.year, t1.genres, t1.boxOffice, t1.numTickets
	FROM Test.dbo.ratings_titles_genres_boxoffice t1, Test.dbo.titles_metacritic t2
	WHERE t1.title = t2.title
	AND t1.year = t2.year
	) t3
;
