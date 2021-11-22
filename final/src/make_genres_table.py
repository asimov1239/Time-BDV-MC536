import pandas as pd

file = open('../data/interim/ratings_titles_genres_boxoffice_metacritic.csv')
lines = file.readlines()

splitlines = list()
for line in lines:
	splitlines.append(line.split(','))

df = pd.DataFrame(columns=['imdb_id', 'genre'])
idx = 0
for line in splitlines:
	_id = line[0]
	genres = line[5:-2]
	for genre in genres:
		df = df.append(pd.DataFrame({'imdb_id': _id, 'genre': genre}, index=[idx]))
		idx += 1

df.to_csv('../data/processed/genres_table.csv', index=False)
