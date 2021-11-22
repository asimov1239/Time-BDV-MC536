import json
import pandas as pd
from pprint import pprint

file  = open('../data/external/studio_data.json')
_str  = file.read()
_json = json.loads(_str)
data  = _json['data']

idx = 0
titles_studios = pd.DataFrame(columns=['imdb_id', 'studio', 'country'])
for datum in data:
    imdb_id = datum['imdb_id']
    studios = datum['production_companies']
    for studio in studios:
        name = studio['name']
        country = studio['origin_country']
        titles_studios = titles_studios.append(pd.DataFrame({'imdb_id': imdb_id, 'studio': name, 'country': country}, index=[idx]))
        idx += 1

titles_studios.to_csv('../data/processed/studios_table.csv', index=False)