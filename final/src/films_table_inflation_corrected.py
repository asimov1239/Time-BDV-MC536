import pandas as pd

inflation_path = '../data/interim/united-states-accumulated-inflation-rate-cpi.csv'
inflation = pd.read_csv(inflation_path)

films_path = '../data/interim/films_table_prev.txt'
films = pd.read_csv(films_path)

def get_accum(year):
	return inflation[inflation['year'] == year].accumulated.values[0]

boxOfficeAdjusted = list()
for idx, row in films.iterrows():
	val = row.boxOffice / get_accum(row.year)
	boxOfficeAdjusted.append(val)
films['boxOfficeAdjusted'] = boxOfficeAdjusted

ticketPriceAdjusted = list()
for idx, row in films.iterrows():
	val = row.boxOfficeAdjusted / row.numTickets
	ticketPriceAdjusted.append(val)
films['ticketPriceAdjusted'] = ticketPriceAdjusted

films.to_csv('../data/processed/films_table.csv', index=False)