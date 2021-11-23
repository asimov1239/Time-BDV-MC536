import math
import pandas as pd

films_path = '../data/processed/films_table.csv'
reviews_path = '../data/processed/reviews_table.csv'

films = pd.read_csv(films_path)

reviews = pd.DataFrame(columns=['imdb_id', 'source', 'rating'])

idx2 = 0
for idx, row in films.iterrows():
	imdb_id = row.imdb_id
	imdb_rating = row.imdb_rating
	metacritic_score = row.metacritic_score
	if not math.isnan(imdb_rating):
		reviews = reviews.append(pd.DataFrame({'imdb_id': imdb_id, 'source': 'IMDb', 'rating': imdb_rating}, index=[idx2]))
		idx2 += 1
	if not math.isnan(metacritic_score):
		reviews = reviews.append(pd.DataFrame({'imdb_id': imdb_id, 'source': 'Metacritic', 'rating': metacritic_score}, index=[idx2]))
		idx2 += 1

films.drop(['imdb_rating', 'metacritic_score'], axis=1, inplace=True)

print(films.head())
print(reviews.head())

films.to_csv(films_path, index=False)
reviews.to_csv(reviews_path, index=False)