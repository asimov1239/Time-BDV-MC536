
# Apresentação do Lab08 - Modelo Lógico e Análise de Dados em Grafos

# Equipe `<Time BDV>` - `<BDV>`
* `<Daniel Credico de Coimbra>` - `<155077>`
* `<Gabriel Bonfim Silva de Moraes>` - `<216111>`
* `<Victor Durço Gomes Bijos>` - `<206508>`

## Modelo Lógico Combinado do Banco de Dados de Grafos
> ![Modelo Lógico de Grafos](images/modelo-logico.png)

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises


### Pergunta/Análise 1
> * Qual o gênero mais isolado?

O gênero mais isolado pode ser determinado por uma métrica de centralidade no grafo dos filmes de maior bilheteria em cada um dos últimos 70 anos.
	Closeness centrality é a propriedade de um nó: a somatória do menores caminhos entre cada par de nós. Os gêneros mais comuns (que aparecem em maior quantidade entre os filmes) tendem a ter uma posição mais central, pois se ligariam com uma quantidade maior de filmes e, por consequência, teriam uma closeness centrality alta. Por outro lado, os gêneros incomuns tendem a ter uma closeness centrality menor, sendo assim menos centrais e mais isolados.
Todavia, não necessariamente o gênero mais comum é o gênero mais central, visto que isso depende da maneira como o grafo se conecta. Por exemplo, um gênero muito comum, mas que costuma ocorrer sozinho (sem coexistência com outros gêneros), provavelmente não seria muito central. Tomemos como exemplo dois gêneros: drama e terror. Podemos analisar a centralidade de ambos os nós. Drama com certeza teria closeness centrality elevada, visto que a maior parte dos filmes possuem elementos dramáticos característicos de se encaixar nesse gênero, de modo que o drama tanto ocorre bastante quanto frequentemente está em conjunto com outros gêneros. Com relação ao terror, são poucos os filmes de alta bilheteria que pertencem a tal gênero, tal como são poucas as combinações de terror com outros gêneros, e dese modo podemos prever que sua closeness centrality seria baixa, portanto, seria um gênero mais isolado.
Em síntese, para encontrar o gênero mais isolado basta determinar qual é o nó do grafo com menor closeness centrality.



### Pergunta/Análise 2
> * Pergunta 2

### Pergunta/Análise 3
> * Pergunta 3
