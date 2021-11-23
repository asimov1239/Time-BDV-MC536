* [TMDb Checker](tmdb-checker)
Em JavaScript, sa a API do TMDB para obter informações sobre os estúdios que produziram os filmes, com seus respectivos países de origem.

* [create_hierarchical_dataset.py](create_hierarchical_dataset.py)
Cria versão hierárquica (em JSON) de nosso *dataset*, que originalmente está em formato tabular.

* [films_table_inflation_corrected.py](films_table_inflation_corrected.py)
Adiciona duas colunas à tabela [FILMS](../data/processed/films_table.csv), produzindo assim a sua versão final. Primeiro, corrige a bilheteria pela inflação acumulada do dólar americano, como descrito no item abaixo. Segundo, calcula o preço unitário real (corrigido pela inflação) dos ingressos daquele filme.

* [get_accumulated_inflation.py](get_accumulated_inflation.py)
Obtém a inflação acumulada ano-a-ano do dólar americano, tomando o ano de 1972 como base, a partir [deste dataset](https://www.macrotrends.net/countries/USA/united-states/inflation-rate-cpi).

* [get_metacritic.py](get_metacritic.py)
Usa *webscraping* para pequisar os filmes e obter suas avaliações Metacritic, caso haja.

* [get_thenumbers.py](get_thenumbers.py)
Usa *webscraping* para pesquisar, ano a ano, as bilheterias e o número de ingressos vendidos dos filmes.

* [make_genres_table.py](make_genres_table.py)
Em Python, usa a biblioteca Pandas para criar a tabela [GENRES](../data/processed/genres_table.csv) listando cada associação de um gênero com um filme, a partir de uma versão anterior da tabela [FILMS](../data/processed/films_table.csv).

* [make_reviews_table.py](make_reviews_table.py)
Em Python, usa a biblioteca Pandas para criar a tabela [REVIEWS](../data/processed/reviews_table.csv) listando cada associação de uma resenha com um filme, a partir de uma versão anterior da tabela [FILMS](../data/processed/films_table.csv).

* [make_studios_table.py](make_studios_table.py)
Em Python, usa a biblioteca Pandas para criar a tabela [STUDIOS](../data/processed/studios_table.csv) listando cada associação de uma estúdio e país com um filme, a partir dos dados gerados pelo IMDb Checker descrito acima.

* [ratings_titles_genres.sql](ratings_titles_genres.sql])
Em SQL, realiza um JOIN unindo dados sobre os gêneros dos filmes e suas avaliações IMDb, ambos obtidos independente da API IMDb.

* [ratings_titles_genres_boxoffice.sql](ratings_titles_genres_boxoffice.sql])
Em SQL, realiza um JOIN unindo dados do JOIN anterior com as bilheterias dos filmes, por sua vez obtidas do *website* The Numbers via *webscraping*, conforme descrito acima.

* [ratings_titles_genres_boxoffice_metacritic.sql](ratings_titles_genres_boxoffice_metacritic.sql])
Em SQL, realiza um JOIN unindo dados do JOIN anterior com as avaliações Metacritic dos filmes, por sua vez obtidas do *website* Metacritic via *webscraping*, conforme descrito acima.
