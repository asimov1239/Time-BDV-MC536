# Projeto SQLflix

# Equipe `Time BDV` - `BDV`
* `Daniel Credico de Coimbra` - `155077`
* `Gabriel Bonfim Silva de Moraes` - `216111`
* `Victor Durço Gomes Bijos` - `206508`

## Resumo do Projeto
> Texto resumindo o projeto.

## Slides da Apresentação
> Link do PDF

## Modelo Conceitual Preliminar

> ![Modelo Conceitual Preliminar](assets/ModeloConceitualPreliminar.png)

## Modelos Lógicos Preliminares

~~~
FILMES: (IMDb ID, filme, ano, orçamento, bilheteria, duração)
RESENHA-FILME: (IMDb ID, fonte, nota)
ESTÚDIO-FILME: (IMDb ID, estúdio, país)
GÊNERO-FILME: (IMDb ID, gênero)
~~~

##### Falta um modelo lógico!!

## Dataset Preliminar a ser Publicado
> Elencar os arquivos/bases preliminares dos datasets serão publicados publicados.

título do arquivo/base | link | breve descrição
----- | ----- | -----
`<título do arquivo/base>` | `<link para arquivo/base>` | `<breve descrição do arquivo/base>`

> Os arquivos finais do dataset publicado devem ser colocados na pasta `data`, em subpasta `processed`. Outros arquivos serão colocados em subpastas conforme seu papel (externo, interim, raw). A diferença entre externo e raw é que o raw é em formato não adaptado para uso. A pasta `raw` é opcional, pois pode ser substituída pelo link para a base original da seção anterior.
> Coloque arquivos que não estejam disponíveis online e sejam acessados pelo notebook. Relacionais (usualmente CSV), XML, JSON e CSV ou triplas para grafos.

## Bases de Dados

título da base | link | breve descrição
----- | ----- | -----
`The Movie Database` | `https://www.themoviedb.org/ (API)` | `O Movie Database (TMDB) é um banco de dados popular e editável pelo usuário para filmes e programas de TV.`
`IMDB Database` | `https://www.imdb.com/ (API)` | `API oficial do IMDB (com grandes restrições de uso)`
`Metacritic (site)` | `https://www.metacritic.com/ (Web scraping)` | `Popular site para reviews de jogos, filmes e séries`
`The Numbers (site)` | `https://www.the-numbers.com/ (Web scraping)` | `Site com  útil serviço de dados financeiros sobre filmes.`

## Operações realizadas para a construção do dataset

> Coloque um link para o arquivo do notebook, programas ou workflows que executam as operações de construção do dataset:
* extração de dados de fontes não estruturadas como, por exemplo, páginas Web
* agregação de dados fragmentados obtidos a partir de API
* integração de dados de múltiplas fontes
* tratamento de dados
* transformação de dados para facilitar análise e pesquisa

> Se for notebook, ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as operações envolverem queries executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Liste aqui as perguntas de pesquisa/análise e respectivas análises.
> Nem todas as perguntas precisam de queries que as implementam.
> É possível haver perguntas em que a solução é apenas descrita para
> demonstrar o potencial da base.
>
### Pergunta/Análise 1
> * Pergunta 1


### Pergunta/Análise 2
> * Pergunta 2


### Pergunta/Análise 3
> * Pergunta 3


