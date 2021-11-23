# Projeto SQLflix

# Equipe `Time BDV` - `BDV`

-   `Daniel Credico de Coimbra` - `155077`
-   `Gabriel Bonfim Silva de Moraes` - `216111`
-   `Victor Durço Gomes Bijos` - `206508`

## Resumo do Projeto

Dataset relacional que integra informações de diversas fontes sobre os 25 filmes com maior bilheteria de cada um dos últimos 50 anos (1972-2021), totalizando um escopo inicial de 1250 filmes. Cada filme está associado a características como código IMDb, ano, avaliação crítica (IMDb e Metacritic), e bilheteria em solo americano corrigida por inflação. Ademais, o dataset possui tabelas relacionando filmes a seus gêneros e aos estúdios que os produziram. Como as perguntas de análise indicarão, o objetivo do dataset é permitir tanto maior compreensão do fenômeno cultural do cinema quanto melhor tomada de decisões sobre a produção de filmes.

## Slides da Apresentação

[Link da apresentação (Google Slides)](slides/final_slides.pdf)

## Modelo Conceitual Preliminar

![Modelo Conceitual Preliminar](assets/conceitual_trabalho.jpeg)

## Modelos Lógicos Preliminares

### Modelo relacional: quatro tabelas

```
FILMS: (imdb_id, title, imdb_rating, metacritic_rating, year, boxOffice, numTickets, boxOfficeAdjusted, ticketPriceAdjusted)
REVIEWS: (imdb_id, source, rating)
STUDIOS: (imdb_id, studio, country)
GENRES: (imdb_id, genre)
```

### Modelo hierárquico: coleção de objetos "filme"

```
{
  imdb_id,
  title,
  year,
  boxOffice,
  numTickets,
  boxOfficeAdjusted,
  ticketPriceAdjusted,
  reviews: {
    source,
    rating
  },
  studios: {
    studio,
    country
  },
  genres: {
    genre
  }
}
```

### Modelo de grafo

```
Nódulo: film (imdb_id: int, title: str, year: int, boxOffice: int, numTickets: int, boxOfficeAdjusted: float, ticketsPriceAdjusted: float)
Nódulo: review (source: str, rating: float).
Nódulo: studio (studio: str, country: str).
Nódulo: genre (genre: str).
Relação: has (review × film).
Relação: belongs (studio × film).
Relação: belongs (genre × film).
```

## Dataset

| título do arquivo/base | link                                                  | breve descrição                                                                                                                                                                                          |
| ---------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FILMS`  | [FILMS](data/processed/films_table.csv) | `Tabela contendo uma linha para cada filme em nosso recorte, informando: código IMDb do filme, título, ano, bilheteria, número de ingressos vendidos, box office em solo americano ajustado por inflação do dolar, e preço do ingresso ajustado pela inflação.` |
| `STUDIOS`  | [STUDIOS](data/processed/studios_table.csv) | `Tabela contendo uma linha para cada estúdio que participou da produção de um filme em nosso recorte, informando: código IMDb do filme, nome do estúdio, e país do estúdio.` |
| `REVIEWS`  | [REVIEWS](data/processed/reviews_table.csv) | `Tabela contendo uma linha para cada resenha, dentre avaliações IMDb e Metacritic (mas isso é expansível no futuro), de cada filme em nosso recorte, informando: código IMDb do filme, fonte da resenha, e nota não-normalizada.` |
| `GENRES`  | [GENRES](data/processed/genres_table.csv) | `Tabela contendo uma linha para cada gênero de cada filme em nosso recorte, informando: código IMDb do filme e o nome do gênero.` |

![Films](assets/films_sample.png)

![Studios](assets/studios_sample.png)

![Reviews](assets/reviews_sample.png)

![Genres](assets/genres_sample.png)

## Bases de Dados

| título da base       | link                                          | breve descrição                                                                                              |
| -------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `The Movie Database` | `https://www.themoviedb.org/ (API)`           | `O Movie Database (TMDB) é um banco de dados popular e editável pelo usuário para filmes e programas de TV.` |
| `IMDB Database`      | `https://datasets.imdbws.com/ (API)`                 | `API oficial do IMDB (com grandes restrições de uso)`                                                        |
| `Metacritic (site)`  | `https://www.metacritic.com/ (Web scraping)`  | `Popular site para reviews de jogos, filmes e séries`                                                        |
| `The Numbers (site)` | `https://www.the-numbers.com/ (Web scraping)` | `Site com útil serviço de dados financeiros sobre filmes.`                                                   |

## Detalhamento do Projeto

Duas formas principais foram utilizadas para coletar dados para o projeto:  *webscraping* e acesso de *API*.
### Webscraping
Como regra geral para webscraping, usamos a linguagem Python junto com a biblioteca *BeautifulSoup* para escanear o arquivo html de uma webpage até encontrar a informação necessária.

~~~ python
import requests
from bs4 import BeautifulSoup
~~~~

### TheNumbers.py
Para o arquivo [TheNumbers.py](src/TheNumbers.py), foi utilizado uma estratégia de rotacionar entre os diversos sites para descobrir a lista de filmes dos últimos cinquenta anos, junto com suas respectivas informações de bilheteria e número de ingressos.

~~~ python
year = 2021
# Essas próximas três linhas são utilizadas para armazenar o conteúdo html de um site em um elemento 'soup' 
url_list = "https://www.the-numbers.com/market/" + str(year) + "/top-grossing-movies"
response_list = requests.get(url_list)
soup = BeautifulSoup(response_list.content, "html.parser")
~~~~
Através do elemento gerado por *soup*, adquirimos toda a informação necessária e depois fazemos um loop diminuindo o valor: 
~~~ python 
for i in range(50) 
    year = 2021 - i
    get_data()
~~~
Onde *get_data()* pode ser substituida pelos elementos que se deseja obter do html. Foi necessário um segundo degrau de webscraping para coletar o nome dos filmes, isso aconteceu devido à alguns erros com relação a filmes de nomes muito grandes com reticências no final. Os nomes acabavam ficando na forma de "Missão Impossível: A ..."

Então, bastou uma outra váriavel para armazenar o url de um site com o efetivo nome completo do filme.
~~~ python
# A string str(j['href']) possui o formato "movie/nome-do-filme#tab=box-office"
url_movie = "https://www.the-numbers.com" + str(j['href'])
response_movie = requests.get(url_movie)
soup_movie = BeautifulSoup(response_movie.content, "html.parser")
# Encontrar o nome do filme e transformar em text:
movie_name = soup_movie.find("h1")
movie_name = movie_name.text[0: len(movie_name) - 7]
~~~

Perfeito, agora é fácil escrever todas as informações coletadas em um arquivo csv.

~~~python
# Abrir um arquivo novo e armazenar o objeto csv.writer
file = open("list.csv", "a", newline="", encoding="utf-8")
writer = csv.writer(file)
(...)
# Usamos a função tuple_add para adicionar todas as informações coletadas na variável tupla e escrever essa váriavel no arquivo
tupla = tuple_add(tupla, year, movie_name, budget, number_tickets)
writer.writerow(tupla)
(...)
# Enfim, fechar o arquivo
file.close()
~~~

### Metacritic.py
*falta escrever o metacritic.py*

###  TMDb Checker 
*falta escrever o TMDB Checker*

### Inflação

Para o ajuste da inflação, encontramos um site que contenha alguns dados para nos ajudar no cálculo: https://www.macrotrends.net/countries/USA/united-states/inflation-rate-cpi

Utilizamos o ano de 1972 como refêrencia e obtemos a inflação acumulada para os próximos cinquenta anos. Com cada um desses valores prontos, podemos dividir o *box-office* do ano pela inflação acumulada e descobrir o valor em comparação ao ano de 1972.

![Imagem da Inflaçao](assets/united-states-inflation.png)



## Evolução do Projeto

O projeto SQLflix foi selecionado dentre algumas idéias por ser o mais interessante e moderno das opções. É muito dificil hoje em dia não se envolver no gigante mercado cinematográfico como consumidor.

A ideia de início não passava de um relacionamento entre filme e bilheteria, procurando analisar o crescimento deles nos últimos cinquenta anos. Foi feito um modelo conceitual básico, o qual foi apresentado para o orientador e acrescentado múltiplas ideias. A possível interação entre número de ingressos vendidos, gênero do filme, produções foi levada em consideração.

Encontrar fontes de dados no início pareceu trivial, contudo a complexidade tornou a crescer. O nível de experiência do grupo em coleta de dados era limitado, então logo aprendemos que nem toda fonte de dados poderia ser gratuita e apenas amostras seriam esperadas na forma de API's.

O próprio site do IMDB nos garantiu apenas uma porção dos dados, enquanto o gratuito API da TMDB nos forneceu uma boa quantidade com algumas informações perdidas.

A ideia de um Webscraping surgiu como opção para conseguir as informações sobre bilheteria e número de ingressos vendidos, além de uma segunda opção de review do Metacritic. Estudamos algumas bibliotecas do Python e conseguimos rodar algoritmos para coletar os dados.

Depois disso, bastava construir efetivamente o modelo relacional. Testamos diversos softwares para construir as tabelas SQL, enfim chegamos à conclusão de que o Microsoft SQL Server era a melhor opção para se seguir. Unindo todos os dados coletados, conseguimos os elementos CSV para converter tudo em SQL no software.



## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

* Pergunta/Análise 1: Modelo de Grafos - Quais os estudios mais presentes na produção de filmes de alta bilheteria nos últimos 50 anos?

Através do modelo de grafos, podemos lidar com relacionamentos entre estúdios e filmes. Em específico, a relação (estúdio) -[:produz]-> filme pode nos mostrar a quantidade de filmes produzidos por um estúdio. Assim, podemos contar a quantidade de relações de produção em um nódulo (estúdio) e descobrir os estúdios mais presentes. Abaixo, apresentamos uma query em Cypher para obter essa resposta.

```
MATCH (a)-[:produz]->(b)
RETURN a, COLLECT(a) as productors
ORDER BY SIZE(productors) DESC LIMIT 10
```

* Pergunta/Análise 2: Modelo Hierárquico - Quais os filmes com produção de maior colaboração internacional?

Na construção de nosso dataset, cruzamos informações vindas da API do The Movie Database (TMDB), do qual obtemos arquivos JSON informando os estúdios que participaram na produção de cada filme, junto com o país de origem de cada estúdio. Dessa forma, será possível percorrer cada um de nossos objetos JSON (correspondentes cada um a um filme) e quantificar quais filmes possuem uma maior quantidade de países diferentes dentro de sua lista interna de estúdios de produção.

* Pergunta/Análise 3: Modelo Relacional - Qual a evolução temporal da quantidade de ingressos média dos filmes de maior sucesso ao longo dos anos?

Agrupando a tabela de filmes por ano, podemos contar a média da bilheteria nominal para cada ano. Ao ordenar a tabela pelo ano, obtém-se a série temporal da bilheteria nominal média. Abaixo, apresentamos uma query em SQL para obter essa série.

```
SELECT AVG(boxOffice), year
FROM movie_table
GROUP BY YEAR
ORDER BY year  DESC;
```
