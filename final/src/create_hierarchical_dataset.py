import json
import pandas as pd
from pprint import pprint

films = pd.read_csv('../data/processed/films_table.csv')
genres = pd.read_csv('../data/processed/genres_table.csv')
reviews = pd.read_csv('../data/processed/reviews_table.csv')
studios = pd.read_csv('../data/processed/studios_table.csv')

idlist = list()
jsonlist = list()

for idx, row in films.iterrows():
	idlist.append(row.imdb_id)
	doc = dict()
	doc['imdb_id'] = row.imdb_id
	doc['title'] = row.title
	doc['year'] = row.year
	doc['boxOffice'] = row.boxOffice
	doc['numTickets'] = row.numTickets
	doc['boxOfficeAdjusted'] = row.boxOfficeAdjusted
	doc['ticketPriceAdjusted'] = row.ticketPriceAdjusted
	jsonlist.append(doc)

for idx in range(len(idlist)):
	_id = idlist[idx]
	doc = jsonlist[idx]
	doc['genres'] = list()
	doc['reviews'] = list()
	doc['studios'] = list()
	for idx2, row in genres.iterrows():
		if row.imdb_id == _id:
			doc['genres'].append(row.genre)
	for idx2, row in reviews.iterrows():
		if row.imdb_id == _id:
			doc['reviews'].append({'source': row.source, 'rating': row.rating})
	for idx2, row in studios.iterrows():
		if row.imdb_id == _id:
			doc['studios'].append({'studio': row.studio, 'country': row.country})

text = pprint({'data': jsonlist})
file = open('hiearchical_model.json', 'w')
file.write(text)
file.close()
