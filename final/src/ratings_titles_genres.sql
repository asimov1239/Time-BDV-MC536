SELECT *
INTO Test.dbo.ratings_titles_genres
FROM (
	SELECT t1.tconst, t1.averageRating, t2.primaryTitle, t2.startYear, t2.genres
	FROM ratings t1, titles_genres t2
	WHERE t1.tconst = t2.tconst
	) t3
;
