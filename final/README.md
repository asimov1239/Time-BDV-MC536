# Projeto SQLflix

# Equipe `Time BDV` - `BDV`

-   `Daniel Credico de Coimbra` - `155077`
-   `Gabriel Bonfim Silva de Moraes` - `216111`
-   `Victor Durço Gomes Bijos` - `206508`

## Resumo do Projeto

Dataset que integra informações de diversas fontes sobre os 25 filmes com maior bilheteria de cada um dos últimos 50 anos, totalizando 1250 filmes. Cada filme está relacionado a gêneros e estúdios, além de ser informado características como ano, avaliação crítica (IMDb e Metacritic), bilhetaria, número de bilhetes vendidos, país de origem, estúdios, e código IMDb. O objetivo é permitir maior compreensão do fenômeno cultural do cinema e melhor tomada de decisões sobre produção de filmes.

## Slides da Apresentação

[Link da apresentação (Google Slides)](slides/prévia_slides.pdf)

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

## Datas Publicado

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

## Detalhamento do Projeto

## Evolução do Projeto

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
