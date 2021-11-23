import pandas as pd

inflation_path = '../data/external/united-states-inflation-rate-cpi.csv'
inflation = pd.read_csv(inflation_path)

for idx, row in inflation.iterrows():
	inflation.loc[idx, 'date'] = row.date[:4]
	inflation.loc[idx, 'inflation'] = 1 + (row.inflation / 100)

accumulated = [1]
for idx, row in inflation.iterrows():
	if row.date != '1972':
		accumulated.append(accumulated[int(row.date) - 1972 - 1] * float(row.inflation))

inflation['accumulated'] = accumulated
inflation.loc[49] = pd.Series({'date': '2021', 'inflation': 'NULL', 'accumulated': '6.189321'})

inflation.to_csv('../data/interim/united-states-accumulated-inflation-rate-cpi.csv', index=False)