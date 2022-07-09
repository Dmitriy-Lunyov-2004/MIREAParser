
import html5lib
from bs4 import BeautifulSoup

def getHTMLtable(text):
    soup = BeautifulSoup(text, 'html5lib')

    table = soup.find('tbody')

    return table
    

