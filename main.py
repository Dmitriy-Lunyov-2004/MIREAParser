

from translate_data import translate_data
from urlListGenerator import url_list_generator

from mirea_parser import getHTMLtable

import json
import requests

import csv

import plotCreator

url_list = None
with open('competitionListUrl.json') as file:
    url_list = url_list_generator(file)

tableOptions = None
with open('tableOptions.json') as file:
    tableOptions = json.load(file)["tableOptions"]

entrant_marks = {}

for url in url_list:
    response = requests.get(url)
    table = getHTMLtable(response.text, tableOptions)

    print(url, ": parsing complete")

    data = translate_data(table)

    print('data translated')

    for f, s in data.items():
        entrant_marks[f] = s

x = list(range(320))
y = [0 for _ in x]

for f, s in entrant_marks.items():
    y[s] += 1

x = x[100:]
y = y[100:]

print('Общее число абитуриентов: ', len(entrant_marks))
cur_sum_marks = 263
print(f'Число абитуриентов с баллами больше {cur_sum_marks}:', sum(y[cur_sum_marks:]))

plotCreator.create_plot(x, y)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL, dialect=csv.excel_tab)
    for i, j in zip(x, y):
        writer.writerow([str(i), str(j)])