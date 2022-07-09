

import requests

from urlListGenerator import url_list_generator
import mirea_parser

url_list = url_list_generator()

url = url_list[0]
response = requests.get(url)

table = mirea_parser.getHTMLtable(response.text)

print(table)

#print(*url_list, sep='\n')