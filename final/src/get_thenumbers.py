import requests
from bs4 import BeautifulSoup
import csv


# Atualiza os valores da tupla
def tuple_add(tup, year, name, money, number_tickets):
    lista = list(tup)
    lista[0] = year
    lista[1] = name
    lista[2] = money
    lista[3] = number_tickets
    tup = tuple(lista)
    return tup

# Arquivo de CSV
file = open("list.csv", "a", newline="", encoding="utf-8")
writer = csv.writer(file)

# Ano e tupla
year = 2021
tupla = ("year", "name", "budget", "tickets_sold")
url_list = "https://www.the-numbers.com/market/" + str(year) + "/top-grossing-movies"
response_list = requests.get(url_list)
soup = BeautifulSoup(response_list.content, "html.parser")
td = soup.find_all('td')
# for tag in td:
#     if "data" in str(tag):
#         print(tag)
#     if "movie" in str(tag):
#         for i in tag:
#             for j in i:
#                 print(j['href'])


# Loopando pelos sites
for i in range(50):
    year = 2021 - i
    url_list = "https://www.the-numbers.com/market/" + str(year) + "/top-grossing-movies"
    response_list = requests.get(url_list)
    soup = BeautifulSoup(response_list.content, "html.parser")

    td = soup.find_all('td')

    aux = 0
    index = 0
    for tag in td:
        if "movie" in str(tag):
            movie = tag.text
            for i in tag:
                for j in i:
                    url_movie = "https://www.the-numbers.com" + str(j['href'])
            response_movie = requests.get(url_movie)
            soup_movie = BeautifulSoup(response_movie.content, "html.parser")
            movie_name = soup_movie.find("h1")
            movie_name = movie_name.text[0: len(movie_name) - 7]
            print(year)
            print(movie_name)
            aux = aux + 1
        if "data" in str(tag):
            if "$" in str(tag):
                budget = tag.text[1:]
                budget = budget.replace(",", "")
                print(budget)
                aux = aux + 1
            elif "," in str(tag):
                number_tickets = tag.text
                number_tickets = number_tickets.replace(",", "")
                print(number_tickets)
                aux = aux + 1
        if aux == 3:
            tupla = tuple_add(tupla, year, movie_name, budget, number_tickets)
            writer.writerow(tupla)
            aux = 0
            index = index + 1
        if index == 25:
            break

file.close()
