import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_metascore(movie_name):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	url = f"https://www.metacritic.com/search/movie/{movie_name}/results"
	try:
		response = requests.get(url, headers=headers)
		binary = response.content
		searchpage = BeautifulSoup(binary, "html.parser")
		movie = searchpage.find(class_ = "result first_result")
		positive_score = movie.find(class_ = "metascore_w medium movie positive")
		mixed_score = movie.find(class_ = "metascore_w medium movie mixed")
		negative_score = movie.find(class_ = "metascore_w medium movie negative")
		rv = ''
		if positive_score is not None:
			rv = positive_score.text
		elif mixed_score is not None:
			rv = mixed_score.text
		elif negative_score is not None:
			rv = negative_score.text
		return rv
	except:
		return ''

df = pd.read_csv('../data/raw/titles_boxoffice.csv', names=['year', 'title', 'boxoffice', 'numTickets'])
scorelist = 'title,metacritic_score\n'
for idx, row in df.iterrows():
	score = get_metascore(row.title)
	text = f"{row.title.strip()},{score}\n"
	scorelist += text
	print(text, end='')
file = open('title_metacritic.txt', 'w')
file.write(scorelist)
file.close()
