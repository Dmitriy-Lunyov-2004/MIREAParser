
import html5lib
from bs4 import BeautifulSoup

def getHTMLtable(text, tableOptions):
    soup = BeautifulSoup(text, 'html5lib')

    table = soup.find('tbody')

    rows = table.find_all('tr')

    database = []

    for r in rows:
        data = {}
        for t in tableOptions:
            cell = r.find('td', class_ = t)
            data[t] = cell.string
        database.append(data)

    return database

            

