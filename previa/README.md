# Projeto SQLflix

# Equipe `Time BDV` - `BDV`

-   `Daniel Credico de Coimbra` - `155077`
-   `Gabriel Bonfim Silva de Moraes` - `216111`
-   `Victor Durço Gomes Bijos` - `206508`

## Resumo do Projeto

Dataset que integra informações de diversas fontes sobre os 25 filmes com maior bilheteria de cada um dos últimos 50 anos, totalizando 1250 filmes. Cada filme está relacionado a gêneros e estúdios, além de ser informado características como ano, avaliação crítica (IMDb e Metacritic), bilhetaria, número de bilhetes vendidos, país de origem, estúdios, e código IMDb. O objetivo é permitir maior compreensão do fenômeno cultural do cinema e melhor tomada de decisões sobre produção de filmes.

## Slides da Apresentação

[Link da apresentação (Google Slides)](https://docs.google.com/presentation/d/1Vr6LKrjrr8X0oHr7gW7Hakeil23GS08EE2XSjtrjvOk/)

## Modelo Conceitual Preliminar

![Modelo Conceitual Preliminar](assets/conceitual_trabalho.jpeg)

## Modelos Lógicos Preliminares

### Modelo relacional: quatro tabelas

```
FILMES: (imdb_id, título, ano, país, bilheteria, número_ingressos_vendidos)
RESENHA-FILME: (imdb_id, fonte, nota)
ESTÚDIO-FILME: (imdb_id, estúdio, país)
GÊNERO-FILME: (imdb_id, gênero)
```

### Modelo hierárquico: coleção de objetos "filme"

```
{
  imdb_id,
  título,
  ano,
  país,
  bilheteria,
  número_ingressos_vendidos,
  resenhas: {
    fonte,
    nota
  },
  estúdios: {
    estúdio,
    país
  },
  gêneros: {
    nome_gênero
  }
}
```

### Modelo de grafo

```
Nódulo: filme (imdb_id: int, título: str, ano: int, país: str, bilheteria: int, número_ingressos_vendidos: int)
Nódulo: resenha (fonte: str, nota: float).
Nódulo: estúdio (nome: str, país: str).
Nódulo: gênero (nome: str).
Relação: possui (resenha × filme).
Relação: pertence (estúdio × filme).
Relação: pertence (gênero × filme).
```

##### Falta um modelo lógico!!

## Dataset Preliminar a ser Publicado

| título do arquivo/base | link                                                  | breve descrição                                                                                                                                                                                          |
| ---------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SQLflix_parcial.PNG`  | [SQLflix parcial](data/processed/SQLflix_parcial.PNG) | `Tabela única contendo uma linha por cada filme no nosso recorte, informando: código IMDb, título, ano, bilheteria, número de ingressos vendidos, avaliação IMDb, avaliação Metacritic, e seus gêneros.` |

## Bases de Dados

| título da base       | link                                          | breve descrição                                                                                              |
| -------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `The Movie Database` | `https://www.themoviedb.org/ (API)`           | `O Movie Database (TMDB) é um banco de dados popular e editável pelo usuário para filmes e programas de TV.` |
| `IMDB Database`      | `https://www.imdb.com/ (API)`                 | `API oficial do IMDB (com grandes restrições de uso)`                                                        |
| `Metacritic (site)`  | `https://www.metacritic.com/ (Web scraping)`  | `Popular site para reviews de jogos, filmes e séries`                                                        |
| `The Numbers (site)` | `https://www.the-numbers.com/ (Web scraping)` | `Site com útil serviço de dados financeiros sobre filmes.`                                                   |

## Operações realizadas para a construção do dataset
-   O script [TMDb Checker](src/tmdb-checker) foi utilizado para interagir com a API do The Movie DB (TMDb) e obter dados sobre os estúdios e, futuramente, o país de origem dos filmes.
-   O script [TheNumbers.py](src/TheNumbers.py) foi utilizado para realizar webscraping e obter dados sobre as bilheterias dos filmes.
-   O script [Metacritic.py](src/Metacritic.py) foi utilizado para realizar webscraping e obter dados sobre as avaliações dos filmes.
-   O notebook [SQL to TSV](notebooks/SQL_to_TSV.ipynb) usa um adaptador Python de SQLite3 para converter arquivos .tsv (tab-separated values) obtidos da API limitada gratuita do IMDb em um arquivo SQL em formato .db. Esses arquivos TSV foram baixados prontos do website do IMDb, contendo informações diversas sobre os filmes.
-   O software SQL Server também foi utilizado para importar arquivos CSV e TSV e transformá-los em tabelas SQL. As queries .sql localizadas em [data/interim](data/interim) foram usados para realizar JOINs, criando novas tabelas que consolidassem os dados encontrados nos arquivos CSV e TSV.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Liste aqui as perguntas de pesquisa/análise e respectivas análises.
> Nem todas as perguntas precisam de queries que as implementam.
> É possível haver perguntas em que a solução é apenas descrita para
> demonstrar o potencial da base.

### Pergunta/Análise 1

> Quais estudios mais presentes na produção de filmes de alta bilheteria nos últimos 50 anos?

### Pergunta/Análise 2

> Qual a evolução temporal da bilheteria nominal média dos filmes de maior sucesso ao longo dos anos?

### Pergunta/Análise 3

> Qual a evolução temporal da quantidade de ingressos média dos filmes de maior sucesso ao longo dos anos?

Com o modelo relacional é fácil obter dados para essa questão. Em primeiro lugar, basta adquirir uma média da bilheteria nominal, depois agrupar todos os filmes conforme o ano em que foram lançados. Enfim, ordená-los pelo ano para observar a mudança no valor da média.

```
SELECT AVG(boxOffice), year
FROM movie_table
GROUP BY YEAR
ORDER BY year  DESC;
```
